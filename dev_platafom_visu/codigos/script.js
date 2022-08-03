function uuid() {
    return 'xxxxxxxx-xxxx-LETICIA-I LOVE YOU-xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
      var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
      return v.toString(16);
    });
  }
  
  var userID=uuid();//something like: "ec0c22fa-f909-48da-92cb-db17ecdb91c5" 
  

function criar(NOME, MESA, CODMUSICA, NOMEMUSICA, CANTOR) {
    let row = document.createElement("tr") /* */
    row.setAttribute('class', 'LinhaTable')
    let contador = 0
    while (contador < 6) {
        let item = document.createElement('td')
        if (contador == 0) {
            let texto = document.createTextNode(NOME)
            item.appendChild(texto)
            row.appendChild(item)
        contador++}

        else if(contador==1){
            let texto = document.createTextNode(MESA)
            item.appendChild(texto)
            row.appendChild(item)
            contador++}

        else if(contador==2){
            let texto = document.createTextNode(CODMUSICA)
            item.appendChild(texto)
            row.appendChild(item)
            contador++}

        else if(contador==3){
            let texto = document.createTextNode(NOMEMUSICA)
            item.appendChild(texto)
            row.appendChild(item)
            contador++}

        else if(contador==4){
            let texto = document.createTextNode(CANTOR)
            item.appendChild(texto)
            row.appendChild(item)
            contador++}
        
         else if(contador==5){
            let imagem = document.createElement('img')
            imagem.setAttribute("src","./imagens/microfone.png")
            imagem.setAttribute("width","40px")
            imagem.setAttribute("onclick",`deletar(${uuid()})`)
            imagem.setAttribute("class","botaoMark")
            item.appendChild(imagem)
            row.appendChild(item)
            contador++}

        else{
            contador++
        }
}
document.getElementById("tabelinha").appendChild(row)
}





function botao() {
    criar('nome',645,5545,'oh casinha linda','chico')
}

function deletar(){
    alert("deu  certo brother")
}