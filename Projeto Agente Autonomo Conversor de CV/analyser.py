

meu_perfil = {
    "hard_skills": {
        "Python": ["python", "py", "fastapi", "flask", "django"],
        "C#": ["c#", "c-sharp", "csharp", "dotnet", ".net", "asp.net", "windows forms", "winforms", "programação voltada a objetos"],
        "SQL": ["sql", "postgresql", "postgres", "mysql", "banco de dados", "bancos de dados", "relacional", "relacionais", "modelagem", "queries", "query"],
        "PHP": ["php", "xampp", "laravel"],
        "Web": ["html", "css", "frontend", "ui/ux"],
        "Docker": ["docker", "containers", "containerização"],
        "Git": ["git", "github", "versionamento", "vcs"]
    },
    "idiomas": {
        "Inglês Fluente": ["inglês", "english", "fluent", "advanced", "avançado"]
    },
    "soft-skills": {
        "Comunicação":["comunicação", "organização", "boa comunicação", "trabalho em equipe"],
        "Formulários":["B2B", "relatório", "relatórios", "documentação", "formulário", "formulários"]

    },
    "local": {
        "Ribeirão Preto":["ribeirão preto", "são paulo", "sp", "remoto", "home office"]
    }
}

def analisar_match_inteligente(texto_vaga):
    texto_vaga = texto_vaga.lower()
    skills_confirmadas = []
    pontos = 0
    total_itens = 0

    # Loop Duplo: categoria (ex: hard_skills) -> item (ex: Python)
    for categoria in meu_perfil:
        for item_real, sinonimos in meu_perfil[categoria].items():
            total_itens += 1 # Soma 1 para cada item que existe no perfil mestre
            if any(s in texto_vaga for s in sinonimos):
                skills_confirmadas.append(item_real)
                pontos += 1

    score = (pontos / total_itens) * 100
    return skills_confirmadas, round(score, 2)

# --- TESTE PRÁTICO ---
vaga_linkedin = """Procuramos Dev .NET em Ribeirão Preto. 
Necessário Inglês avançado para leitura de documentação técnica. 
Desejável conhecimento em bancos relacionais e Docker."""
skills, score = analisar_match_inteligente(vaga_linkedin)

print(f"Match Score: {score}%")
print(f"O bot encontrou: {skills}")


def gerar_curriculo_otimizado(skills_confirmadas):
    print("\n--- PLANO DE GERAÇÃO DE PDF ---")
    for categoria in meu_perfil["hard_skills"]:
        if categoria in skills_confirmadas:
            print(f"[ MANTER ] {categoria} -> Relevante para a vaga.")
        else:
            print(f"[ OMITIR ] {categoria} -> Irrelevante para esta vaga.")

# Chamando a nova função usando o resultado que você acabou de obter
gerar_curriculo_otimizado(skills)

