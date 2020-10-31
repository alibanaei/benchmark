<?php

function main(array $args){
    $number = $args["number"] ?? 5;

    $start = time();

    $r = 1;
    for($i = 1; $i < $number+1; $i++){
        $r *= $i;
    }

    $end = time();
    $time = $end - $start;

    return ["time" => $time];
}