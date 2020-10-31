<?php

function generate_matrix($size){
    $matrix = array();

    for($i = 0; $i < $size; $i++){
        $matrix[$i] = array();
        for($j = 0; $j < $size; $j++){
            $matrix[$i][$j] = rand(0, 999);
        }
    }

    return $matrix;
}

function multiply_matrices($m1, $m2, $size){
    $result = array();
    for($i = 0; $i < $size; $i++){
        $matrix[$i] = array();
        for($j = 0; $j < $size; $j++){
            $matrix[$i][$j] = 0;
        }
    }

    for($i = 0; $i < $size; $i++){
        for($j = 0; $j < $size; $j++){
            $sum = 0;
            for($k = 0; $k < $size; $k++){
                $sum += $m1[$i][$k] * $m2[$k][$j];
            }

            $result[$i][$j] = $sum;
        }
    }

    return $result;
}

function main($args){
    $size = $args["size"] ?? 50;

    $start = time();
    $m1 = generate_matrix($size);
    $m2 = generate_matrix($size);
    $result = multiply_matrices($m1, $m2, $size);

    $end = time();
    $time = $end - $start;
    return ["time" => $time, "result" => count($result)];
}