// 알고리즘 자체는 맞는 거 같은데 js가 큰 숫자 처리를 못 함

const fs = require('fs');
let input = Number(fs.readFileSync('/dev/stdin').toString().trim());
const MOD_BILLION = 1000000000;

let fibo = [0 , 1]; // 0 1 1 2 3 5 8
// let fiboMinus = [0 , 1];  0 1 -1 2 -3 5 -8 13 -21

for (let i = 0; i < 1000000 - 1; i++){
    fibo.push(fibo[i] + fibo[i + 1]);
}

// for (i = 0; i < 1000000 - 1; i++) { 
//     fiboMinus.push(fiboMinus[i] - fibo[i + 1]);
// }

if (input === 0) {
    console.log(0);
    console.log(0);
} else if (input < 0 && input % 2 == 0) {
    console.log(-1);
    console.log(fibo[Math.abs(input)] % MOD_BILLION);
} else { 
    console.log(1);
    console.log(fibo[Math.abs(input)] % MOD_BILLION);
}
