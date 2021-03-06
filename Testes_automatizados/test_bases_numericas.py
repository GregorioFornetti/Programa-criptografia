from Cifras import bases_numericas
import dicionarios

# BINÁRIO - TEXTOS
def test_binario_trocar_um_caractere_minusculo():
    assert bases_numericas.transformar_texto_para_binario('a') == '1100001'
    assert bases_numericas.transformar_binario_para_texto('1100001') == 'a'

def test_binario_trocar_um_caractere_maiusculo():
    assert bases_numericas.transformar_texto_para_binario('A') == '1000001'
    assert bases_numericas.transformar_binario_para_texto('1000001') == 'A'

def test_binario_trocar_um_caractere_especial():
    assert bases_numericas.transformar_texto_para_binario('á') == '11100001'
    assert bases_numericas.transformar_binario_para_texto('11100001') == 'á'

def test_binario_traducao_invalido_1():
    assert bases_numericas.transformar_binario_para_texto('1111210') == dicionarios.retorna_erro_mensagem()

def test_binario_traducao_invalido_2():
    assert bases_numericas.transformar_binario_para_texto('1111111111111111111111111') == dicionarios.retorna_erro_mensagem()

def test_binario_mensagem_invalida():
    assert bases_numericas.transformar_texto_para_binario('') == dicionarios.retorna_erro_mensagem()
    assert bases_numericas.transformar_binario_para_texto('') == dicionarios.retorna_erro_mensagem()

def test_binario_texto_grande_1():
    assert bases_numericas.transformar_texto_para_binario('Primeiro texto em binário'
    ) == '1010000 1110010 1101001 1101101 1100101 1101001 1110010 1101111 100000 1110100 1100101 1111000 1110100 1101111 100000 1100101 1101101 100000 1100010 1101001 1101110 11100001 1110010 1101001 1101111'

    assert bases_numericas.transformar_binario_para_texto(
    '1010000 1110010 1101001 1101101 1100101 1101001 1110010 1101111 100000 1110100 1100101 1111000 1110100 1101111 100000 1100101 1101101 100000 1100010 1101001 1101110 11100001 1110010 1101001 1101111'
    ) == 'Primeiro texto em binário'

def test_binario_texto_grande_2():
    assert bases_numericas.transformar_texto_para_binario('Caracteres especiais:*Ü¡˟ɮ'
    ) == '1000011 1100001 1110010 1100001 1100011 1110100 1100101 1110010 1100101 1110011 100000 1100101 1110011 1110000 1100101 1100011 1101001 1100001 1101001 1110011 111010 101010 11011100 10100001 1011011111 1001101110'

    assert bases_numericas.transformar_binario_para_texto(
    '1000011 1100001 1110010 1100001 1100011 1110100 1100101 1110010 1100101 1110011 100000 1100101 1110011 1110000 1100101 1100011 1101001 1100001 1101001 1110011 111010 101010 11011100 10100001 1011011111 1001101110'
    ) == 'Caracteres especiais:*Ü¡˟ɮ'

# BINÁRIO - CONVERSÕES DIRETAS
def test_binario_para_octal_1():
    assert bases_numericas.converter_binario_para_octal('101101') == '55'

def test_binario_para_octal_2():
    assert bases_numericas.converter_binario_para_octal('1111101110') == '1756'

def test_binario_para_decimal_1():
    assert bases_numericas.converter_binario_para_decimal('101001') == 41

def test_binario_para_decimal_2():
    assert bases_numericas.converter_binario_para_decimal('111011011') == 475

def test_binario_para_hexadecimal_1():
    assert bases_numericas.converter_binario_para_hexadecimal('11011010') == 'DA'

def test_binario_para_hexadecimal_2():
    assert bases_numericas.converter_binario_para_hexadecimal('11000110110') == '636'

def test_verificacao_binario():
    assert bases_numericas.verificar_num_bin('11101101 100111') == False
    assert bases_numericas.verificar_num_bin('111011210110') == False
    assert bases_numericas.verificar_num_bin('110111opa') == False
    assert bases_numericas.verificar_num_bin('11101011\n') == False
    assert bases_numericas.verificar_num_bin('1011011101101111') == True

# OCTAL - TEXTOS
def test_octal_trocar_um_caractere_minusculo():
    assert bases_numericas.transformar_texto_para_octal('a') == '141'
    assert bases_numericas.transformar_octal_para_texto('141') == 'a'

def test_octal_trocar_um_caractere_maiusculo():
    assert bases_numericas.transformar_texto_para_octal('A') == '101'
    assert bases_numericas.transformar_octal_para_texto('101') == 'A'

def test_octal_trocar_um_caractere_especial():
    assert bases_numericas.transformar_texto_para_octal('á') == '341'
    assert bases_numericas.transformar_octal_para_texto('341') == 'á'

def test_octal_traducao_invalido_1():
    assert bases_numericas.transformar_octal_para_texto('1238') == dicionarios.retorna_erro_mensagem()

def test_octal_traducao_invalido_2():
    assert bases_numericas.transformar_octal_para_texto('77777777777') == dicionarios.retorna_erro_mensagem()

def test_octal_mensagem_invalida():
    assert bases_numericas.transformar_texto_para_octal('') == dicionarios.retorna_erro_mensagem()
    assert bases_numericas.transformar_octal_para_texto('') == dicionarios.retorna_erro_mensagem()

def test_octal_texto_grande_1():
    assert bases_numericas.transformar_texto_para_octal('Primeiro texto em octal'
    ) == '120 162 151 155 145 151 162 157 40 164 145 170 164 157 40 145 155 40 157 143 164 141 154'

    assert bases_numericas.transformar_octal_para_texto(
    '120 162 151 155 145 151 162 157 40 164 145 170 164 157 40 145 155 40 157 143 164 141 154'
    ) == 'Primeiro texto em octal'

def test_octal_texto_grande_2():
    assert bases_numericas.transformar_texto_para_octal('Caracteres especiais:*Ü¡˟ɮ'
    ) == '103 141 162 141 143 164 145 162 145 163 40 145 163 160 145 143 151 141 151 163 72 52 334 241 1337 1156'

    assert bases_numericas.transformar_octal_para_texto(
    '103 141 162 141 143 164 145 162 145 163 40 145 163 160 145 143 151 141 151 163 72 52 334 241 1337 1156'
    ) == 'Caracteres especiais:*Ü¡˟ɮ'

def test_verificacao_octal():
    assert bases_numericas.verificar_num_octal('15105 1341') == False
    assert bases_numericas.verificar_num_octal('124101481304') == False
    assert bases_numericas.verificar_num_octal('145a6167') == False
    assert bases_numericas.verificar_num_octal('12461246\n') == False
    assert bases_numericas.verificar_num_octal('1515302637142356412345670') == True

# OCTAL - CONVERSÕES DIRETAS
def test_octal_para_binario_1():
    assert bases_numericas.converter_octal_para_binario('123') == '1010011'

def test_octal_para_binario_2():
    assert bases_numericas.converter_octal_para_binario('6141') == '110001100001'
    assert bases_numericas.converter_octal_para_binario('0') == '0'

def test_octal_para_decimal_1():
    assert bases_numericas.converter_octal_para_decimal('12') == 10

def test_octal_para_decimal_2():
    assert bases_numericas.converter_octal_para_decimal('341') == 225

def test_octal_para_hexadecimal_1():
    assert bases_numericas.converter_octal_para_hexadecimal('142') == '62'

def test_octal_para_hexadecimal_2():
    assert bases_numericas.converter_octal_para_hexadecimal('1402') == '302'

# DECIMAL - TEXTOS
def test_decimal_trocar_um_caractere_minusculo():
    assert bases_numericas.transformar_texto_para_decimal('a') == '97'
    assert bases_numericas.transformar_decimal_para_texto('97') == 'a'

def test_decimal_trocar_um_caractere_maiusculo():
    assert bases_numericas.transformar_texto_para_decimal('A') == '65'
    assert bases_numericas.transformar_decimal_para_texto('65') == 'A'

def test_decimal_trocar_um_caractere_especial():
    assert bases_numericas.transformar_texto_para_decimal('á') == '225'
    assert bases_numericas.transformar_decimal_para_texto('225') == 'á'

def test_decimal_traducao_invalido_1():
    assert bases_numericas.transformar_decimal_para_texto('1238a') == dicionarios.retorna_erro_mensagem()

def test_decimal_traducao_invalido_2():
    assert bases_numericas.transformar_decimal_para_texto('99999999999999') == dicionarios.retorna_erro_mensagem()

def test_decimal_mensagem_invalida():
    assert bases_numericas.transformar_texto_para_decimal('') == dicionarios.retorna_erro_mensagem()
    assert bases_numericas.transformar_decimal_para_texto('') == dicionarios.retorna_erro_mensagem()

def test_decimal_texto_grande_1():
    assert bases_numericas.transformar_texto_para_decimal('Primeiro texto em decimal'
    ) == '80 114 105 109 101 105 114 111 32 116 101 120 116 111 32 101 109 32 100 101 99 105 109 97 108'

    assert bases_numericas.transformar_decimal_para_texto(
    '80 114 105 109 101 105 114 111 32 116 101 120 116 111 32 101 109 32 100 101 99 105 109 97 108'
    ) == 'Primeiro texto em decimal'

def test_decimal_texto_grande_2():
    assert bases_numericas.transformar_texto_para_decimal('Caracteres especiais:*Ü¡˟ɮ'
    ) == '67 97 114 97 99 116 101 114 101 115 32 101 115 112 101 99 105 97 105 115 58 42 220 161 735 622'

    assert bases_numericas.transformar_decimal_para_texto(
    '67 97 114 97 99 116 101 114 101 115 32 101 115 112 101 99 105 97 105 115 58 42 220 161 735 622'
    ) == 'Caracteres especiais:*Ü¡˟ɮ'

# DECIMAL - CONVERSÕES DIRETAS
def test_decimal_para_binario_1():
    assert bases_numericas.converter_decimal_para_binario(24) == '11000'

def test_decimal_para_binario_2():
    assert bases_numericas.converter_decimal_para_binario(102) == '1100110'

def test_decimal_para_octal_1():
    assert bases_numericas.converter_decimal_para_octal(42) == '52'

def test_decimal_para_octal_2():
    assert bases_numericas.converter_decimal_para_octal(140) == '214'

def test_decimal_para_hexadecimal_1():
    assert bases_numericas.converter_decimal_para_hexadecimal(52) == '34'

def test_decimal_para_hexadecimal_2():
    assert bases_numericas.converter_decimal_para_hexadecimal(184) == 'B8'

def test_verificacao_decimal():
    assert bases_numericas.verificar_num_decimal('1210424 12') == False
    assert bases_numericas.verificar_num_decimal('1924014a132') == False
    assert bases_numericas.verificar_num_decimal('1032120\n') == False
    assert bases_numericas.verificar_num_decimal('1234567890') == 1234567890

# HEXADECIMAL - TEXTOS
def test_hexadecimal_trocar_um_caractere_minusculo():
    assert bases_numericas.transformar_texto_para_hexadecimal('a') == '61'
    assert bases_numericas.transformar_hexadecimal_para_texto('61') == 'a'

def test_hexadecimal_trocar_um_caractere_maiusculo():
    assert bases_numericas.transformar_texto_para_hexadecimal('A') == '41'
    assert bases_numericas.transformar_hexadecimal_para_texto('41') == 'A'

def test_hexadecimal_trocar_um_caractere_especial():
    assert bases_numericas.transformar_texto_para_hexadecimal('á') == 'E1'
    assert bases_numericas.transformar_hexadecimal_para_texto('E1') == 'á'

def test_hexadecimal_traducao_invalido_1():
    assert bases_numericas.transformar_hexadecimal_para_texto('1ABCDEFG') == dicionarios.retorna_erro_mensagem()

def test_hexadecimal_traducao_invalido_2():
    assert bases_numericas.transformar_hexadecimal_para_texto('FFFFFFFFF') == dicionarios.retorna_erro_mensagem()

def test_hexadecimal_mensagem_invalida():
    assert bases_numericas.transformar_texto_para_hexadecimal('') == dicionarios.retorna_erro_mensagem()
    assert bases_numericas.transformar_hexadecimal_para_texto('') == dicionarios.retorna_erro_mensagem()

def test_hexadecimal_texto_grande_1():
    assert bases_numericas.transformar_texto_para_hexadecimal('Primeiro texto em hexadecimal'
    ) == '50 72 69 6D 65 69 72 6F 20 74 65 78 74 6F 20 65 6D 20 68 65 78 61 64 65 63 69 6D 61 6C'

    assert bases_numericas.transformar_hexadecimal_para_texto(
    '50 72 69 6D 65 69 72 6F 20 74 65 78 74 6F 20 65 6D 20 68 65 78 61 64 65 63 69 6D 61 6C'
    ) == 'Primeiro texto em hexadecimal'

def test_hexadecimal_texto_grande_2():
    assert bases_numericas.transformar_texto_para_hexadecimal('Caracteres especiais:*Ü¡˟ɮ'
    ) == '43 61 72 61 63 74 65 72 65 73 20 65 73 70 65 63 69 61 69 73 3A 2A DC A1 2DF 26E'

    assert bases_numericas.transformar_hexadecimal_para_texto(
    '43 61 72 61 63 74 65 72 65 73 20 65 73 70 65 63 69 61 69 73 3A 2A DC A1 2DF 26E'
    ) == 'Caracteres especiais:*Ü¡˟ɮ'

# HEXADECIMAL - CONVERSÕES DIRETAS
def test_hexadecimal_para_binario_1():
    assert bases_numericas.converter_hexadecimal_para_binario('46') == '1000110'

def test_hexadecimal_para_binario_2():
    assert bases_numericas.converter_hexadecimal_para_binario('A1c') == '101000011100'
    assert bases_numericas.converter_hexadecimal_para_binario('0') == '0'

def test_hexadecimal_para_octal_1():
    assert bases_numericas.converter_hexadecimal_para_octal('52') == '122'

def test_hexadecimal_para_octal_2():
    assert bases_numericas.converter_hexadecimal_para_octal('C4a') == '6112'

def test_hexadecimal_para_decimal_1():
    assert bases_numericas.converter_hexadecimal_para_decimal('62') == 98

def test_hexadecimal_para_decimal_2():
    assert bases_numericas.converter_hexadecimal_para_decimal('Fa1') == 4001

def test_verificacao_hexadecimal():
    assert bases_numericas.verificar_num_hexadecimal('14912AB 184AB') == False
    assert bases_numericas.verificar_num_hexadecimal('1234401EFG') == False
    assert bases_numericas.verificar_num_hexadecimal('1234561abc\n') == False
    assert bases_numericas.verificar_num_hexadecimal('0123456789ABCDEF') == True
    assert bases_numericas.verificar_num_hexadecimal('0123456789abcdef') == True
