import os
from openai import OpenAI


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY", ""))


def analisar_descricao_vaga(descricao):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Modelo gratuito
            messages=[
                {"role": "system", "content": "Você é um assistente inclusivo."},
                {"role": "user", "content": f"Por favor, analise e sugira melhorias:\n\n{descricao}"},
            ],
            temperature=0.5,
            max_tokens=1000,
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"Erro ao usar o modelo gpt-3.5-turbo: {e}"


if __name__ == "__main__":
    print("Bem-vindo ao Analisador de Descrição de Vagas Inclusivas!")
    print("Por favor, insira a descrição da vaga (digite 'fim' para encerrar):")
    descricao_vaga = []
    while True:
        linha = input()
        if linha.strip().lower() == "fim":
            break
        descricao_vaga.append(linha)


    descricao_vaga = "\n".join(descricao_vaga).strip()
    if not descricao_vaga:
        print("Nenhuma descrição fornecida.")
    else:
        resultado = analisar_descricao_vaga(descricao_vaga)
        print("\nResultado da análise com IA:")
        print(resultado)
