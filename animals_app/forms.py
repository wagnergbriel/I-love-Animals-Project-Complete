from django import forms

class ColaboradorForm(forms.Form):
    nome = forms.CharField(label="Digite seu nome:", max_length=200)
    numero_celular = forms.CharField(label="Digite o numero do seu telefone:", max_length=14)
    email = forms.EmailField(label="Digite seu email:")
    senha = forms.CharField(label="Digite sua senha:", max_length=12)
    tipo_identificacao_pessoal = forms.CharField(label="Escolha o tipo de identificação:",
        max_length=14, choices=TipoIdentificacaoPessoal.choices, default="CNPJ"
    )
    identificador_pessoal = forms.CharField(label="Digite o tipo de identificação:", max_length=14)
    endereco = forms.CharField(label="Digite seu endereço:", max_length=200)
    numero_endereco = forms.IntegerField(label="Digite o número do endereço:")
    cep = forms.CharField(label="Digite o cep", max_length=8)
    estado = forms.CharField(label="Escolha o seu estado:",
        max_length=10, choices=[(state, state) for state in ufbr.list_uf]
    )
    cidade = forms.CharField(label="Escolha o sua cidade:", max_length=200)
    bairro = forms.CharField(label="Escolha o seu bairro:", max_length=200)
    complemento = forms.CharField(label="Escolha o complemento:", max_length=500)