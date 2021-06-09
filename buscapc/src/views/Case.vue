<template>
<div class="field is-grouped">
  <div class="control">
        <label class="label">Marca  </label>
        <div class="select is-small">
          <select name="LeaveType" @change="fetchList()" class="form-control" v-model="filtros.marca">
            <option value=""></option>
            <option value="corsair">Corsair</option>
            <option value="redragon">Redragon</option>
            <option value="thermaltake">Thermaltake</option>
            <option value="dt3_sports">DT3</option>
            <option value="cooler_master">Cooler Master</option>
            <option value="t-dagger">T-Dagger</option>
            <option value="pcyes">PCYes</option>
            <option value="nzxt">NZXT</option>
            <option value="cougar">Cougar</option>
            <option value="pichau_gaming">Pichau</option>
            <option value="aigo">Aigo</option>
            <option value="aerocool">AeroCool</option>
            <option value="deepcool">DeepCool</option>
          </select>
        </div>
  </div>
     
    
   <div class="control">
      <label class="label">Tamanho </label>
      <div class="select is-small">
        <select name="LeaveType" @change="fetchList()" class="form-control" v-model="filtros.tamanho">
            <option value=""></option>
            <option value="Mid Tower">Mid Tower</option>
            <option value="Full Tower">Full Tower</option>
            <option value="ITX">ITX</option>
            <option value="mATX">mATX</option>
            <option value="ATX">ATX</option>
        </select>
      </div>
  </div>

</div>
  <div class="row">
      <div class="col-12">        
          <table class="table table-hover">
          <tr> 
            <th></th>
            <th>Nome</th>
            <th>Marca</th>
            <th>Tamanho</th>
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
            <td><img v-bind:src="product.img" style="width:150px;height:90px;"> </td>
            <td><a :href="product.link">{{ product.nome }}</a></td>
            <td>{{ product.marca }}</td>
            <td>{{ product.tamanho }}</td>
            <td>R${{ product.preco }}</td>
            <td>
                <button v-on:click="addCase(product.link)" class="button is-light">Adicionar</button>
            </td>
            <td></td>
          </tr>
        </table>
      </div>         
    </div>
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
        "nvme":"",
        "sata":"",
        "link":""
      }
    };
  },
  created: function() {
      this.fetchList();
  },

  methods: {
    fetchList(){
        const mybody = {"tipo":"case", "filtros":this.filtros}
        axios.post("http://localhost:3003/db", mybody)
        .then((response) => {
        this.produtos = response.data;
        this.loading = false})
    }, 
    addCase(caseLink){
        const mybody = {"tipo":"case", "link":caseLink}
        axios.post("http://localhost:3003/db/add", mybody)
        .then((response) => {
          if (response.data.adicionado){
            alert("Produto adicionado!")
          }
          else{
            alert("Voce ja possui um produto deste tipo na lista!")
          }
        })
    }
  }
};
</script>
