#include <stdio.h>
int main ()
{
    int linhasColunas;
    printf ("Quantos vertices tem ? ");
    scanf ("%i",&linhasColunas );
    int matriz [linhasColunas][linhasColunas];
     
    for (int i = 0; i < linhasColunas; i++)
    {
        for (int j = 0; j < linhasColunas; j++)
        {
            printf ("Qual eh o peso da aresta de %i para %i ", (i+1) , (j+1));
            scanf ("%i", &matriz [i][j]);
        }
        
    }

    for (int i = 0; i < linhasColunas; i++)
    {
        for (int j = 0; j < linhasColunas; j++)
        {
            printf ("%i ", matriz [i][j]);            
        }
        printf ("\n");
        
    }








}