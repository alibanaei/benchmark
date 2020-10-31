<?php

function fib($n){
    if($n < 2) return $n;

    return fib($n -1 ) + fib ($n - 2);
}

function main(array $args){
    $number = $args["number"] ?? 5;

    $start = time();
    $result = fib($number);
    $end = time();
    $time = $end - $start;
    return ["time" => $time, "result" => $result];
}