<template>
  <div class="field is-grouped">
      <div class="control">
        <label class="label">Marca  </label>
        <div class="select is-small">
          <select name="LeaveType" @change="fetchList()" class="form-control" v-model="filtros.marca">
            <option value=""></option>
            <option value="asrock">ASRock</option>
            <option value="asus">ASUS</option>
            <option value="gigabyte">Gigabyte</option>
            <option value="biostar">Biostar</option>
            <option value="msi">MSI</option>
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
            <option value="LGA1151">LGA1151</option>
            <option value="LGA1200">LGA1200</option>
            <option value="TRX4">TRX4</option>
        </select>
      </div>
    </div>

    <div class="control">
      <label class="label">DDR </label>
      <div class="select is-small">
        <select name="LeaveType" @change="fetchList()" class="form-control" v-model="filtros.ddr">
            <option value=""></option>
            <option value="DDR3">DDR3</option>
            <option value="DDR4">DDR4</option>
        </select>
      </div>
    </div>    

  </div>
  <div class="row">
      <div class="col-12">        
          <table class="table is-striped">
          <tr> 
            <th></th>
            <th>Nome</th>
            <th>Marca</th>
            <th>Chipset</th>
            <th>Socket</th>
            <th>Tamanho</th>
            <th>DDR</th>
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
            <td><img v-bind:src="product.img" style="width:120px;height:90px;"> </td>
            <td><a :href="product.link">{{ product.nome }}</a></td>
            <td>{{ product.marca }}</td>
            <td>{{ product.chipset }}</td>
            <td>{{ product.socket }}</td>
            <td>{{ product.tamanho }}</td>
            <td>{{ product.ddr }}</td>
            <td>R${{ product.preco }}</td>
            <td>
                <button v-on:click="addMobo(product.link)" class="button is-light">Adicionar</button>
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
        const mybody = {"tipo":"mobo", "filtros":this.filtros}
        axios.post("http://localhost:3003/db", mybody)
        .then((response) => {
        this.produtos = response.data;
        this.loading = false})
    }, 
    addMobo(moboLink){
        const mybody = {"tipo":"mobo", "link":moboLink}
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
