class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        letras_verificadas = []
        maior = 0

        for letra in s:
            if letra not in letras_verificadas:
                letras_verificadas.append(letra)
                maior = max(maior, len(letras_verificadas))
            else:

                indice = letras_verificadas.index(letra)
                letras_verificadas = letras_verificadas[indice + 1:]
                letras_verificadas.append(letra)

        return maior
