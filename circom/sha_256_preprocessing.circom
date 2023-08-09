// pre-poccessing the inpit message
// input: assume all the input has already been transform as binary, and the input string is L bits
// function operation:
// 1. append a single '1' bit
// 2. culculate # k need to be appended, L + 1 + k + 64 is a multiple of 512
// 3. append L as a 64-bit big-endian integer

pragma circom 2.0.0;

template padding(L) {
    // input: L = length of msg

    signal input msg[L];
    // culculate # block in the string after padding
    var num_of_block = cul_num_of_block(L);
    signal output str_after_padding[num_of_block * 512];
    var i;

    // fill in origin string into str_after_padding
    for (i = 0; i < L; i ++){
        str_after_padding[i] <== msg[L];
    }
    // append a single '1' bit
    str_after_padding[L] <== 1;
    // append '0'
    for (i = L + 1; i < num_of_block * 512 - 64; i++){
        str_after_padding[i] <== 0;
    } 
    // append L as a binary
    for (i = 1; i < 65; i++){
        str_after_padding[num_of_block * 512 - i] <== (L >> i) & 1
    }
}

function cul_num_of_block(L){
    return (L+1+64)\512 + 1;
}

