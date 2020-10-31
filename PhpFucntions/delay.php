<?php

function main(array $args){
    $number = $args["number"] ?? 10;

    sleep($number);

    return ["time" => $number];
}