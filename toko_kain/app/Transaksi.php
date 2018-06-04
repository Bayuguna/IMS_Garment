<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Transaksi extends Model
{
    protected $table = 'tb_transaksi';
    public $timestamps = false;

    public function jenis(){
        return $this->hasOne('App\Jenis', 'jenis');
    }
}
