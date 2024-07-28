#include <stdio.h>


int add(int a, int b)
{
	return (a + b);
}
int main()
{
	//printf("\n\nBrand new repository for GitHub");
	int a= 4, b=6, sum;
	sum = add(a,b);
	printf("\nsum= %d", sum);
	return 0;
}

/*
gcc -shared -fdiagnostics-color=always -g main.c -o "${fileDirname}\\${fileBasenameNoExtension}.dll" -fPIC
*/