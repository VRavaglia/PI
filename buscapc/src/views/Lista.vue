<template>   
  <table class="table is-stripped">
    <tr> 
      <th></th>
      <th></th>
      <th>Nome</th>
      <th>Preço</th>
      <th></th>
      <th></th>
    </tr>
    <tr>
      <td colspan="5" v-show="loading==true">Carregando produtos...</td>
    </tr>
    <tr v-if="produtos.length == 0 && loading==false">
      <td colspan="5">Nenhum produto para exibir!</td>
    </tr>
    <tr v-for="(product, index) in produtos" :key="product.id">
      <td></td>
      <td><img v-bind:src="product.img" style="width:100px;height:90px;"> </td>
      <td><a :href="product.link">{{ product.nome }}</a></td>
      <td>R${{ product.preco }}</td>
      <td>
          <button v-on:click="removePeca(product.link)" class="button is-light">Remover</button>
      </td>
      <td></td>
    </tr>
  </table>
        

</template>

<script>

import axios from "axios"
export default {  
  data() {
    return {
      loading: true,
      produtos: [],
      produto: {
        name: '',
        value: ''
      },
      precoTotal: 0,
      filtros: {
        "marca":"",
        "socket":"",
        "tamanho":"",
        "ddr": "",
        "capacidade":"",
        "vram":"",
        "integrada":"",
        "fabricante":"",
        "ssd":"",
        "frequencia":"",
        "selo":"",
        "link":""
      }
    };
  },
  created: function() {
      this.fetchList();
      
  },

  methods: {
    fetchList(){
        const mybody = {"tipo":"hd", "filtros":this.filtros}
        axios.get("http://localhost:3003/db")
        .then((response) => {
        this.produtos = response.data;
        this.loading = false})
    }, 
    removePeca(pecaLink){
        const mybody = {"link":pecaLink}
        axios.post("http://localhost:3003/db/remove", mybody)
        .then((response) => {
            this.fetchList();
        })
    }
  }
};
</script>

