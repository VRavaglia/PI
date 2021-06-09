<template>
<div class="field is-grouped">
  <div class="control">
        <label class="label">Marca  </label>
        <div class="select is-small">
          <select name="LeaveType" @change="fetchList()" class="form-control" v-model="filtros.marca">
            <option value=""></option>
            <option value="wd">WD</option>
            <option value="seagate">Seagate</option>
            <option value="toshiba">Toshiba</option>
            <option value="pny">PNY</option>
            <option value="team_group">Team Group</option>
            <option value="gigabyte">Gigabyte</option>
            <option value="corsair">Corsair</option>
            <option value="xpg">XPG</option>
            <option value="pichau_gaming">Pichau</option>

          </select>
        </div>
  </div>
     
  <div class="control">
      <label class="label">SSDs</label>
      <div class="select is-small">
        <select name="LeaveType" @change="fetchList()" class="form-control" v-model="filtros.ssd">
            <option value=""></option>
            <option value=1>Sim</option>
            <option value=0>Nao</option>
        </select>
      </div>
  </div>

  <div class="control">
      <label class="label">NVMEs</label>
      <div class="select is-small">
        <select name="LeaveType" @change="fetchList()" class="form-control" v-model="filtros.nvme">
            <option value=""></option>
            <option value=1>Sim</option>
            <option value=0>Nao</option>

        </select>
      </div>
  </div>

  <div class="control">
      <label class="label">SATAs</label>
      <div class="select is-small">
        <select name="LeaveType" @change="fetchList()" class="form-control" v-model="filtros.sata">
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
            <th>Dimensoes</th>
            <th>Capacidade</th>
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
            <td>{{ product.dimensoes }}</td>
            <td>{{ product.capacidade }}</td>
            <td>R${{ product.preco }}</td>
            <td>
                <button v-on:click="addFonte(product.link)" class="button is-light">Adicionar</button>
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
        const mybody = {"tipo":"hd", "filtros":this.filtros}
        axios.post("http://localhost:3003/db", mybody)
        .then((response) => {
        this.produtos = response.data;
        this.loading = false})
    }, 
    addFonte(fonteLink){
        const mybody = {"tipo":"hd", "link":fonteLink}
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
