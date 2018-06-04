<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Toko Kain</title>
    <link rel="stylesheet" href="css/app.css">
    <script src="js/app.js"></script>
    <script src="jquery/jquery.min.js"></script>
    <script src="/jquery-easing/jquery.easing.min.js"></script>
    <link rel="stylesheet" href="font-awesome/css/font-awesome.css">
</head>
<body>
    
        
        <div class="card">
            <div class="card-header" style="text-align: center">
                <h1>TOKO KAIN</h1>

            </div>
            <div class="row col-md-12">
        <form action="/toko" method="POST" >
        {{csrf_field()}}
                <div class="card-body">
                <div class="col-md-5">
                    <div class="form-group">
                        <label for="exampleInputEmail1">Jenis Kain</label>
                        <select id="jenis" name="jenis" class="form-control jenis" required>
                                <option value="">Jenis Kain</option>
                                @foreach($jenis as $row)
                                <option value="{{$row->jenis}}">{{$row->jenis}}</option>
                                @endforeach
                            </select>
                    </div>

                    <div class="form-group">
                        <label for="exampleInputEmail1">Kwalitas Kain</label>
                        <select id="kwalitas" name="kwalitas" class="form-control" aria-describedby="emailHelp" placeholder="Kwalitas Kain" required>
                            <option value="">Kwalitas Kain</option>
                            @foreach($kwalitas as $row)
                            <option value="{{$row->nama}}">{{$row->nama}}</option>
                            @endforeach
                        </select>
                    </div>

                    <div class="form-group">
                        <label for="exampleInputEmail1">Tekstur Kain</label>
                        <input type="text" name="tekstur" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Tekstur Kain" required>
                    </div>

                    <div class="form-group">
                        <label for="exampleInputEmail1">Warna Kain</label>
                        <input type="text" name="warna" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Warna Kain" required>
                    </div>

                    <div class="form-group">
                        <label for="exampleInputEmail1">Panjang Kain (meter)</label>
                        <input type="text" name="panjang" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Panjang Kain" required>
                    </div>

                    <div class="form-group">
                        <label for="exampleInputEmail1">Harga</label>
                        <input type="text" id="harga" name="harga" class="form-control" aria-describedby="emailHelp" placeholder="Harga" required>
                    </div>
                    
                    <button type="submit" class="btn btn-primary pull-right">Simpan</button>
                </div>
            </div>
        </form>

            <div class="col-md-7" style="margin-top: 30px">
                    <table class="table table-bordered">
                    <thead class="thead-dark">
                        <tr>
                        <th scope="col">ID</th>
                        <th scope="col">Jenis Kain</th>
                        <th scope="col">Kwalitas Kain</th>
                        <th scope="col">Tekstur Kain</th>
                        <th scope="col">Warna Kain</th>
                        <th scope="col">Panjang Kain (m)</th>
                        <th scope="col">Harga</th>
                        <th scope="col">Action</th>
                        </tr>
                    </thead>
                    <tbody>
                        @foreach($trans as $row)
                        <tr>
                        <th scope="row">{{$row->id}}</th>
                        <td>{{$row->jenis_kain}}</td>
                        <td>{{$row->kwalitas_kain}}</td>
                        <td>{{$row->tekstur_kain}}</td>
                        <td>{{$row->warna_kain}}</td>
                        <td>{{number_format($row->panjang_kain)}}</td>
                        <td>{{number_format($row->harga)}}</td>
                        <td>
                            <button type="button" data-toggle="modal" data-target="#editModal_{{$row->id}}" class="btn btn-success">
                                <i class="fa fa-pencil-square-o"></i>
                            </button>
                            <button type="button" data-toggle="modal" data-target="#deleteModal_{{$row->id}}" class="btn btn-danger">
                                <i class="fa fa-trash"></i>
                            </button>

                            <!-- Modal -->
                            <div class="modal fade" id="editModal_{{$row->id}}" tabindex="-1" role="dialog">
                            <div class="modal-dialog" role="document">
                                <div class="modal-content">
                                <div class="modal-header">
                                    <h5 class="modal-title">Edit</h5>
                                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                    <span aria-hidden="true">&times;</span>
                                    </button>
                                </div>
                                <div class="modal-body">
                                    <form action="/toko/{{$row->id}}" method="POST" >
                                    {{csrf_field()}}
                                    {{method_field('PUT')}}
                                                <div class="form-group">
                                                    <label for="exampleInputEmail1">Jenis Kain</label>
                                                    <input type="text" name="jenis" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" value="{{$row->jenis_kain}}" required autofocus>
                                                </div>
                            
                                                <div class="form-group">
                                                    <label for="exampleInputEmail1">Kwalitas Kain</label>
                                                    <input type="text" name="kwalitas" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" value="{{$row->kwalitas_kain}}" required>
                                                </div>
                            
                                                <div class="form-group">
                                                    <label for="exampleInputEmail1">Tekstur Kain</label>
                                                    <input type="text" name="tekstur" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" value="{{$row->tekstur_kain}}" required>
                                                </div>
                            
                                                <div class="form-group">
                                                    <label for="exampleInputEmail1">Warna Kain</label>
                                                    <input type="text" name="warna" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" value="{{$row->warna_kain}}" required>
                                                </div>
                            
                                                <div class="form-group">
                                                    <label for="exampleInputEmail1">Panjang Kain (meter)</label>
                                                    <input type="text" name="panjang" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" value="{{$row->panjang_kain}}" required>
                                                </div>
                            
                                                <div class="form-group">
                                                    <label for="exampleInputEmail1">Harga</label>
                                                    <input type="text" name="harga" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" value="{{$row->harga}}" required>
                                                </div>
                                                
                                                <button type="submit" class="btn btn-success pull-right">Edit</button>
                                    </form>
                                </div>
                                </div>
                            </div>
                            </div>

                            <!--Modal-->
                            <div class="modal fade" id="deleteModal_{{$row->id}}" tabindex="-1" role="dialog">
                            <div class="modal-dialog" role="document">
                                <div class="modal-content">
                                <div class="modal-header">
                                    <h5 class="modal-title">Hapus</h5>
                                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                    <span aria-hidden="true">&times;</span>
                                    </button>
                                </div>
                                <div class="modal-body">
                                    <h5>Hapus Transaksi</h5>
                                </div>
                                <div class="modal-footer">
                                        <form action="/toko/{{$row->id}}" method="POST">
                                            {{csrf_field()}}
                                            {{method_field('DELETE')}}
                                        <button type="submit" class="btn btn-danger">Hapus</button>
                                        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                                        </form>
                                        
                                </div>
                                </div>
                            </div>
                            </div>

                                        </div>
                                    </div>
                                    </div>
                                </div>
                        </td>
                        </tr>
                        @endforeach
                    </tbody>
                    </table>
                    
                    
            </div>
            </div>
            
        </div>
<script>
    $(document).ready(function(){
        $("#jenis").on('change', function(){
        if($(this).val() != ''){
            var name = $("#jenis").val();
            // console.log(name)

            $.ajax({
                url:"/data?q="+name,
                dataType: "json",
                success:function(value){
                $("#harga").val(value.harga);
                // console.log(value)
                }
        });
        }else{
            // console.log("kosongin...")
            $("#harga").val("");
        }
        });

        $("#kwalitas").on('change', function(){
            if($("#jenis").val() != ''){
            var name = $("#jenis").val();
            // console.log(name)

            $.ajax({
                url:"/data?q="+name,
                dataType: "json",
                success:function(value){
                    if($("#kwalitas").val() == 'Original'){
                        $("#harga").val(number_format(value.harga));
                    }else if($("#kwalitas").val() == 'KW super'){
                        $("#harga").val(value.harga/2);
                    }else if($("#kwalitas").val() == 'KW Biasa'){
                        $("#harga").val(value.harga/3);
            }
                // console.log(value)
                }
        });
        }else{
            // console.log("kosongin...")
            $("#harga").val("");
        }
        })
    });
</script>
</body>
</html>