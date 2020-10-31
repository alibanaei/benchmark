<?php

function main($args){
    $number = $args["number"] ?? 10000000;
    $start = time();

    $result = [];
    for($i = 0; $i < $number; $i++)
        $result[$i] = $i;

    $end = time();
    $time = $end - $start;


    return ["time" => $time, "result" => count($result)];
}
