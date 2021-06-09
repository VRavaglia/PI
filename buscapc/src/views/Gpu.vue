<template>
<div class="field is-grouped">
  <div class="control">
        <label class="label">Marca  </label>
        <div class="select is-small">
          <select name="LeaveType" @change="fetchList()" class="form-control" v-model="filtros.marca">
            <option value=""></option>
            <option value="asus">ASUS</option>
            <option value="asrock">ASRock</option>
            <option value="gigabyte">Gigabyte</option>
            <option value="sapphire">Sapphire</option>
            <option value="mancer">Mancer</option>
            <option value="powercolor">Powercolor</option>
            <option value="zotac">ZOTAC</option>
            <option value="galax">Galax</option>
            <option value="pny">PNY</option>

          </select>
        </div>
  </div>
     
    
   <div class="control">
      <label class="label">Fabricante </label>
      <div class="select is-small">
        <select name="LeaveType" @change="fetchList()" class="form-control" v-model="filtros.fabricante">
            <option value=""></option>
            <option value="nvidia">Nvidia</option>
            <option value="amd">AMD</option>

        </select>
      </div>
  </div>

  <div class="control">  
      <label class="label">VRAM </label>
      <div class="select is-small">
        <select name="LeaveType" @change="fetchList()" class="form-control" v-model="filtros.vram">
            <option value=""></option>
            <option value=2>2GB</option>
            <option value=4>4GB</option>
            <option value=6>6GB</option>
            <option value=8>8GB</option>
            <option value=12>12GB</option>
            <option value=16>16GB</option>
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
            <th>Fabricante</th>
            <th>VRAM</th>
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
            <td>{{ product.fabricante }}</td>
            <td>{{ product.vram }}</td>
            <td>R${{ product.preco }}</td>
            <td>
                <button v-on:click="addGpu(product.link)" class="button is-light">Adicionar</button>
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
        const mybody = {"tipo":"gpu", "filtros":this.filtros}
        axios.post("http://localhost:3003/db", mybody)
        .then((response) => {
        this.produtos = response.data;
        this.loading = false})
    }, 
    addGpu(gpuLink){
        const mybody = {"tipo":"gpu", "link":gpuLink}
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
