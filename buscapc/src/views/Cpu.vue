<template>
  <div class="field is-grouped">
      <div class="control">
        <label class="label">Marca  </label>
        <div class="select is-small">
          <select name="LeaveType" @change="fetchList()" class="form-control" v-model="filtros.marca">
            <option value=""></option>
            <option value="amd">AMD</option>
            <option value="intel">Intel</option>

          </select>
        </div>
      </div>
    
    <div class="control">
      <label class="label">Socket </label>
      <div class="select is-small">
        <select name="LeaveType" @change="fetchList()" class="form-control" v-model="filtros.socket">
            <option value=""></option>
            <option value="FM2">FM2</option>
            <option value="AM4">AM4</option>
            <option value="LGA 1151">LGA1151</option>
            <option value="LGA1200">LGA1200</option>
            <option value="TRX4">TRX4</option>
        </select>
      </div>
    </div>

    <div class="control">
      <label class="label">Integrada </label>
      <div class="select is-small">
        <select name="LeaveType" @change="fetchList()" class="form-control" v-model="filtros.integrada">
            <option value=""></option>
            <option value=1>Sim</option>
            <option value=0>Nao</option>
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
            <th>Socket</th>
            <th>Frequencia</th>
            <th>Integrada</th>
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
            <td><img v-bind:src="product.img" style="width:220px;height:90px;"> </td>
            <td><a :href="product.link">{{ product.nome }}</a></td>
            <td>{{ product.marca }}</td>
            <td>{{ product.socket }}</td>
            <td>{{ product.frequencia }}</td>
            <td>{{ product.integrada }}</td>
            <td>R${{ product.preco }}</td>
            <td>
                <button v-on:click="addCpu(product.link)" class="button is-light">Adicionar</button>
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
        const mybody = {"tipo":"cpu", "filtros":this.filtros}
        axios.post("http://localhost:3003/db", mybody)
        .then((response) => {
        this.produtos = response.data;
        this.loading = false})
    }, 
    addCpu(cpuLink){
        const mybody = {"tipo":"cpu", "link":cpuLink}
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
