class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        palavra = s
        letras_verificadas= []
        maior = 0

        for letra in palavra:
            if letra not in letras_verificadas:
                letras_verificadas.append(letra)
            else:
                maior = len(letras_verificadas)
        return maior