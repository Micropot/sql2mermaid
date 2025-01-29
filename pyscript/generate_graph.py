from pyscript import document
from sql2mermaid.sql2mermaid import mermaid_generator


# def generate_graph(event):
#     input_text = document.querySelector("#mermaid-code")
#     sql_query = input_text.value
#     output_div = document.querySelector("#output")
#     output_div.innerText = mermaid_generator(sql_query)
def generate_graph(event):
    input_text = document.querySelector("#mermaid-code")
    print("input", input_text)
    sql_query = input_text.value
    output_div = document.querySelector("#output")

    # Effacer l'ancien contenu
    output_div.innerHTML = ""

    # Créer un nouvel élément pour le diagramme
    mermaid_div = document.createElement("div")
    mermaid_div.setAttribute("class", "mermaid")
    mermaid_div.innerText = mermaid_generator(sql_query)

    # Ajouter au conteneur
    output_div.appendChild(mermaid_div)
