# 21. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.
def to_uppercase(str1):
    num_upper = 0
    for letter in str1[:4]:
        if letter.upper( ) == letter:
            num_upper += 1
    if num_upper >= 2:
        return str1.upper( )
    return str1


print(to_uppercase('Toiyeuseal'))
print(to_uppercase('ToiYeuseal'))


# 22.Write a Python program to sort a string lexicographically.
def lexicographic_sort(s):
    return sorted(sorted(s), key = str.upper)


print(lexicographic_sort('bocchankawaii'))
print(lexicographic_sort('justkikiguy'))

# 23. Write a Python program to remove a newline in Python.
str1 = 'Seal\aDthWa\a\aĐi'
cleaned_text = str1.replace('\a', '')
print(cleaned_text)

# 24. Write a Python program to check whether a string starts with specified characters.
string = 's3aLb0cCh4n'
print(string.startswith('s3a'))


# 25. Write a Python program to create a Caesar encryption.
# Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.
def caesar_encrypt(realText, step):
    outText = []
    cryptText = []
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
    for eachLetter in realText:
        if eachLetter in uppercase:
            index = uppercase.index(eachLetter)
            crypting = (index + step) % 26
            cryptText.append(crypting)
            newLetter = uppercase[crypting]
            outText.append(newLetter)
        elif eachLetter in lowercase:
            index = lowercase.index(eachLetter)
            crypting = (index - step) % 26
            cryptText.append(crypting)
            newLetter = lowercase[crypting]
            outText.append(newLetter)
    return outText


code = caesar_encrypt('abc', 2)
print( )
print(code)
print( )

# 26. Write a Python program to display formatted text (width=50) as output.
import textwrap

sample_text = '''
右から左へとマグロが流れる	
おいしそうな顔　大間から来た君
築地の壁越えていつでも食べに行く	
赤身の準備をちゃんとしておいてね
君のこと何一つ知らない	
だから関係ないけど	
とりあえずまあ二人で踊りましょう
たこルカ★マグロフィーバー	
ゆるゆるリズムに合わせて	
嫌なこと何もかも全部忘れて	
たこルカ★マグロフィーバー	
私は軟体動物	
たこやきに入れたら	
おいしいけどダメダメよ☆
'''
print( )
print(textwrap.fill(sample_text, width = 50))
print( )

# 27. Write a Python program to remove existing indentation from all of the lines in a given text.
import textwrap

sample_text = '''
誰かの想いが立ち昇る にわか雨が街を濡らし始めた 夕暮れ時
傘を持たない女の子 その黒髪濡らしとこへ行く 橋の向こう
バスが遠い街へ 走り去れば
あぁ 今夜 どこへ行こうか 沈む街 何もないけど
あぁ 今夜 どこへ行こうか 人並みは交差して
季節の終わり 空の広がる涙
窓際の席に座り込んで 僕は何に想いを馳せよう ひとりきり
にごったままさお茶の水 でもそのまま喉に流しこもう ガラス越し
'''
text_without_Indentation = textwrap.dedent(sample_text)
print( )
print(text_without_Indentation)
print( )

# 28. Write a Python program to add prefix text to all of the lines in a string.
import textwrap

sample_text = '''
Rêve de moi, amour perdu
Rêve de moi s'il neigera
Je suis vent et nostalgie
Je suis où tu vas
'''
text_without_Indentation = textwrap.dedent(sample_text)
wrapped = textwrap.fill(text_without_Indentation, width = 50)
final_result = textwrap.indent(wrapped, '>')
print( )
print(final_result)
print( )

# 29. Write a Python program to set the indentation of the first line.
import textwrap

sample_text = '''
You could've asked me why I broke your heart
You could've told me that you fell apart
But you walked past me like I wasn't there
And just pretended like you didn't care
'''
text1 = textwrap.dedent(sample_text).strip( )
print( )
print(textwrap.fill(text1,
                    initial_indent = ' ',
                    subsequent_indent = ' ' * 4,
                    width = 80,
                    ))
print( )

# 30. Write a Python program to print the following numbers up to 2 decimal places.
x = 28.1205071401
y = 2.31106
print( )
print('Original Number:', x)
print('Formatted Number:' + '{:.2f}'.format(x))
print('Original Number:', y)
print('Formatted Number:' + '{:.2f}'.format(y))
print( )
