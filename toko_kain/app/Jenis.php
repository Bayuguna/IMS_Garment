<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Jenis extends Model
{
    protected $table = 'tb_jenis_kain';
    public $timestamps = false;

    public function transaksi(){
        return $this->belongsTo('App\Transaksi', 'jenis_kain');
    }
}
