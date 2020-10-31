<?php


function get_nth_prime_number($n){
    $num = 2;
    for($i = 0; $i < $n; $i++)
        $num = get_next_prime_number($num);

    return $num;
}

function get_next_prime_number($n){
    for($i = $n + 1; $i < $n * $n; $i++)
        if(is_prime($i))
            return $i;

        return 0;
}

function is_prime($n){
    for($i = 2; $i < $n; $i++)
        if($n % $i == 0)
            return False;
    return True;
}

function main(array $args){
    $num = $args["number"] ?? 0;

    $start = time();

    $result = get_nth_prime_number($num);

    $end = time();

    $time = $end - $start;

    return ["time" => $time, "result" => $result];
}