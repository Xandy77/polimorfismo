import classes as cl

if __name__ == '__main__':
    # entrada de dados
    nome = input('Informe o nome do usuário: ')
    email = input('Informe o email do usuário: ')
    cpf = input('Informe o cpf do usuário: ')
    profissao = input('Informe a profissão do usuário: ')
    endereco = input('Informe o endereco do usuário: ')
    telefone = input('Informe o telefone do usuário: ')


    # instancia a classe pessoa física
    usuario =  cl.PessoaFisica(nome, cpf, profissao, endereco, email, telefone)

    # entrada de dados
    nome = input('Informe o nome da Empresa: ')
    email = input('Informe o email da Empresa: ')
    cnpj = input('Informe o cnpj da Empresa: ')
    razao_social = input('Informe a razao_social da Empresa: ')
    endereco = input('Informe o endereco da Empresa: ')
    telefone = input('Informe o telefone da Empresa: ')


    # instancia a classe pessoa juridica
    empresa = cl.PessoaJuridica(nome, razao_social, cnpj, endereco, email, telefone)

    # saída de dados
    usuario.mostrar_cartao_visitas()
    print('-'*30)
    empresa.mostrar_cartao_visitas()






