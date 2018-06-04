<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Transaksi;
use App\Kwalitas;
use App\Jenis;
use DB;

class TransaksiController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        $trans = Transaksi::all();
        $kwalitas = Kwalitas::all();
        $jenis = Jenis::all();

        return view('index', compact('trans', 'kwalitas', 'jenis'));
    }

    public function loadData(Request $request){
        if ($request->has('q')) {
    		$cari = $request->q;
            $data = Jenis::select('id', 'jenis', 'harga')->where('jenis', 'LIKE', '%' .$cari. '%')->first();
            
            return $data;
    		return response()->json($data);
    }
}

    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        //
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        $trans = new Transaksi;

        $trans->jenis_kain = $request->jenis;
        $trans->kwalitas_kain = $request->kwalitas;
        $trans->tekstur_kain = $request->tekstur;
        $trans->warna_kain = $request->warna;
        $trans->panjang_kain = $request->panjang;
        $trans->harga = $request->harga;
        $trans->save();

        return redirect('/toko');
    }

    /**
     * Display the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function show($id)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function edit($id)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, $id)
    {
        $trans = Transaksi::find($id);

        $trans->jenis_kain = $request->jenis;
        $trans->kwalitas_kain = $request->kwalitas;
        $trans->tekstur_kain = $request->tekstur;
        $trans->warna_kain = $request->warna;
        $trans->panjang_kain = $request->panjang;
        $trans->harga = $request->harga;
        $trans->save();

        return redirect('/toko');
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function destroy($id)
    {
        Transaksi::where('id', $id)->delete();

        return redirect('/toko');
    }
}
