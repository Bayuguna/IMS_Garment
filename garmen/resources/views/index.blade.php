<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Garment</title>
    <link rel="stylesheet" href="css/app.css">
    <script src="js/app.js"></script>
    <script src="jquery/jquery.js"></script>
    <link rel="stylesheet" href="font-awesome/css/font-awesome.css">
    
</head>
<body>
        <div class="card">
            <div class="card-header" style="text-align: center">
                <h1>GARMENT</h1>

            </div>

            <div class="col-md-7" style="margin: 30px 0px 0px 320px">
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
                            <button type="button" class="btn btn-info" data-toggle="modal" data-target="#showModal_{{$row->id}}" >
                                <i class="fa fa-eye"></i>
                            </button>

                            <!-- Modal -->
                            <div class="modal fade" id="showModal_{{$row->id}}" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                                <div class="modal-dialog" role="document">
                                <div class="modal-content">
                                    
                                    <div class="modal-body" style="text-align: center">
                                        <form action="/garmen" method="POST" >
                                            {{csrf_field()}}
                                                        <div class="form-group">
                                                            <label for="exampleInputEmail1">Ukuran S</label>
                                                        <input type="text" name="jenis" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" value="{{number_format(($row->panjang_kain))}}" readonly>
                                                        </div>
                                    
                                                        <div class="form-group">
                                                            <label for="exampleInputEmail1">Ukuran M<Link:css></Link:css></label>
                                                            <input type="text" name="kwalitas" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" value="{{number_format(($row->panjang_kain)/2)}}" readonly>
                                                        </div>
                                    
                                                        <div class="form-group">
                                                            <label for="exampleInputEmail1">Ukuran L</label>
                                                            <input type="text" name="tekstur" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" value="{{number_format(($row->panjang_kain)/3)}}" readonly>
                                                        </div>
                                    
                                                        <div class="form-group">
                                                            <label for="exampleInputEmail1">Ukuran XL</label>
                                                            <input type="text" name="warna" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" value="{{number_format(($row->panjang_kain)/4)}}" readonly>
                                                        </div>
                                            </form>
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
</body>
</html>