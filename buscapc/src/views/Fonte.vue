<template>
<div class="field is-grouped">
  <div class="control">
        <label class="label">Marca  </label>
        <div class="select is-small">
          <select name="LeaveType" @change="fetchList()" class="form-control" v-model="filtros.marca">
            <option value=""></option>
            <option value="corsair">Corsair</option>
            <option value="azza">AZZA</option>
            <option value="pichau_gaming">Pichau</option>
            <option value="tgt">TGT</option>
            <option value="cooler_master">Cooler Master</option>
            <option value="super_flower">Super Flower</option>
            <option value="cougar">Cougar</option>
            <option value="seasonic">Seasonic</option>
            <option value="mancer">Mancer</option>
            <option value="duex">Duex</option>
            <option value="hoopson">Hoopson</option>
            <option value="aerocool">AeroCool</option>
            <option value="evga">EVGA</option>
            <option value="c3_tech">C3 Tech</option>

          </select>
        </div>
  </div>
     
  <div class="control">
      <label class="label">Selo</label>
      <div class="select is-small">
        <select name="LeaveType" @change="fetchList()" class="form-control" v-model="filtros.selo">
            <option value=""></option>
            <option value="80 Plus">80 Plus</option>
            <option value="80 Plus White">80 Plus White</option>
            <option value="80 Plus Bronze">80 Plus Bronze</option>
            <option value="80 Plus Gold">80 Plus Gold</option>
            <option value="80 Plus Platinum">80 Plus Platinum</option>
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
            <th>Selo</th>
            <th>Potencia</th>
            <th>Modularidade</th>
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
            <td>{{ product.selo }}</td>
            <td>{{ product.potencia }}</td>
            <td>{{ product.modularidade }}</td>
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
        const mybody = {"tipo":"psu", "filtros":this.filtros}
        axios.post("http://localhost:3003/db", mybody)
        .then((response) => {
        this.produtos = response.data;
        this.loading = false})
    }, 
    addFonte(fonteLink){
        const mybody = {"tipo":"psu", "link":fonteLink}
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
