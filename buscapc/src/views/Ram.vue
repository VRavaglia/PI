<template>
<div class="field is-grouped">
  <div class="control">
        <label class="label">Marca  </label>
        <div class="select is-small">
          <select name="LeaveType" @change="fetchList()" class="form-control" v-model="filtros.marca">
            <option value=""></option>
            <option value="xpg">XPG</option>
            <option value="hyperx">HyperX</option>
            <option value="corsair">Corsair</option>
            <option value="g_skill">G-Skill</option>
            <option value="lexar">Lexar</option>
            <option value="crucial">Crucial</option>
            <option value="team_group">Team Group</option>
            <option value="kingston">Kingston</option>

          </select>
        </div>
  </div>
     
    
   <div class="control">
      <label class="label">Capacidade </label>
      <div class="select is-small">
        <select name="LeaveType" @change="fetchList()" class="form-control" v-model="filtros.capacidade">
            <option value=""></option>
            <option value=2>2GB</option>
            <option value=4>4GB</option>
            <option value=8>8GB</option>
            <option value=16>16GB</option>
            <option value=32>32GB</option>

        </select>
      </div>
  </div>

  <div class="control">
      <label class="label">Frequencia</label>
      <div class="select is-small">
        <select name="LeaveType" @change="fetchList()" class="form-control" v-model="filtros.frequencia">
            <option value=""></option>
            <option value=1333>1333MHz</option>
            <option value=1600>1600MHz</option>
            <option value=1866>1866MHz</option>
            <option value=2133>2133MHz</option>
            <option value=2400>2400MHz</option>
            <option value=2666>2666MHz</option>
            <option value=3000>3000MHz</option>
            <option value=3200>3200MHz</option>
            <option value=3600>3600MHz</option>
            <option value=4133>4133MHz</option>  

        </select>
      </div>
  </div>

  <div class="control">  
      <label class="label">DDR </label>
      <div class="select is-small">
        <select name="LeaveType" @change="fetchList()" class="form-control" v-model="filtros.ddr">
            <option value=""></option>
            <option value="DDR3">DDR3</option>
            <option value="DDR3L">DDR3L</option>
            <option value="DDR4">DDR4</option>
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
            <th>Capacidade</th>
            <th>Frequencia</th>
            <th>DDR</th>
            <th>Quantidade</th>
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
            <td><img v-bind:src="product.img" style="width:250px;height:90px;"> </td>
            <td><a :href="product.link">{{ product.nome }}</a></td>
            <td>{{ product.marca }}</td>
            <td>{{ product.capacidade }}</td>
            <td>{{ product.frequencia }}</td>
            <td>{{ product.ddr }}</td>
            <td>{{ product.quantidade }}</td>
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
        const mybody = {"tipo":"ram", "filtros":this.filtros}
        axios.post("http://localhost:3003/db", mybody)
        .then((response) => {
        this.produtos = response.data;
        this.loading = false})
    }, 
    addGpu(ramLink){
        const mybody = {"tipo":"ram", "link":ramLink}
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
