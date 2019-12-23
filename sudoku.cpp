// Template taken from https://github.com/glapul/contest_library/blob/master/template.cpp
#include<bits/stdc++.h>	
using namespace std;

#define db(x) (cerr << #x << ": " << (x) << "\n")
#define sync ios_base::sync_with_stdio(false), cin.tie(NULL)    // speedup i/o with cin/cout

bool conflict(vector<vector<char> > &A, int r, int c, char val){
    for(int i = 0; i < 9; i++){
        if(A[i][c] == val) return true;
        if(A[r][i] == val) return true;
    }
    
    int r1 = (r/3)*3, r2 = r1 + 2;
    int c1 = (c/3)*3, c2 = c1 + 2;
    for(int i = r1; i <= r2; i++){
        for(int j = c1; j <= c2; j++){
            if(A[i][j] == val){
                return true;
            }
        }
    }
    
    return false;
    
}

void sudoku(vector<vector<char> >&A, vector<vector<char> >&B, int r, int c){
    if(B.size() == 0){
        int k, i = r, j = c;
        
        if(j == 9) {
            i++; 
            j = 0;
        }
        
        while(i < 9 && A[i][j] != '0'){
            while(j < 9 && A[i][j] != '0'){
                j++;
            }
            if (j == 9) {
                i++; j = 0;
            }
        }
        if(i == 9) B = A;
        else{
            for(k = 1; k <= 9 && B.size() == 0;  k++){
                if(!conflict(A, i, j, char(48+k))){
                    A[i][j] = char(48+k);
                    sudoku(A, B, i, j+1);
                    A[i][j] = '0';    
                }   
            }
        }
    }
}

void solveSudoku(vector<vector<char> > &A) {
    vector<vector<char> >ans;
    sudoku(A, ans, 0, 0);
    A.clear();
    A = ans;
}

main(){
    #ifndef DEBUG
            freopen("./input.txt", "r", stdin);
            freopen("./output.txt", "w", stdout);
    #endif
	sync;
    clock_t clk = clock();
    vector<vector<char> > board(9, vector<char> (9));
    for(int i = 0; i < 9; i++){
    	for(int j = 0; j < 9; j++){
    		cin >> board[i][j];
    	}
    }

    solveSudoku(board);
	
	for(int i = 0; i < 9; i++){
    	for(int j = 0; j < 9; j++){
    		cout << board[i][j] << " ";
    	}
    	cout << endl;
    }    

    cerr << "Time (in ms): " << (double)(clock() - clk) * 1000.0 / CLOCKS_PER_SEC << "\n";
}
