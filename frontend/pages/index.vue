<template>
  <section class="section">
    <div class="button">
      <a href="/charts">
        <button>Посмотреть графики</button>
      </a>
      <input type="text" placeholder="Поиск" v-on:keyup.enter="search" v-model="text">
    </div>
    <div class="map">
        <client-only>
            <v-map :zoom="options.minZoom" :center="center">
                <l-tile-layer :url="map"></l-tile-layer>
                  <v-marker-cluster>
                        <template v-for="(object, i) in objects">
                          <v-marker @click="ShowMarker(object)"  :lat-lng="[object.longitude, object.latitude]" :key="i"></v-marker>
                        </template>
                  </v-marker-cluster>
            </v-map>
        </client-only>
    </div>
    <div class="blck" v-if="objectItem">
      <div class="head">
        <h1>Информация об объекте</h1>
        <button @click="CloseMarker()">Закрыть</button>
      </div>
      <span><b>Название:</b> {{objectItem.name}}</span>
      <span><b>Адрес:</b> {{objectItem.addres}} </span>
      <span><b>Описание:</b> {{objectItem.discShort}}</span>
    </div>
  </section>
</template>

<script>
export default {

  data: () => ({
    objects: [],
    objectItem: null,
    text: "",
    options: {
        minZoom: 3,
        maxZoom: 18,
    },
    center: [61, 73],
    map: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
}),
methods: {
  async resp(){
    try{
      await this.$axios.get("/objects").then(response => (this.objects = response.data));
        console.log(this.objects)
    }
    catch (e) {
      console.log(e)
    }
  },
  async ShowMarker(object) {
      this.objectItem = object;
  },
  async CloseMarker() {
      this.objectItem = null;
  },
  async search() {
    try {
      await this.$axios.get(`/objects?search=${this.text}`).then(response => (this.objects = response.data));
        console.log(this.objects)
    }
    catch (e) {
      console.log(e)
    }
  }
},

mounted() {
  this.resp()
}
}
</script>

<style>
  .head {
    display: flex;
    width: 100%;
    justify-content: space-between;
  }
  .button {
    position: absolute;
    right: 20px;
    top: 20px;
    z-index: 999;
    display: flex;
    flex-direction: row-reverse;
  }
  input {
    padding-left: 10px;
    width: 200px;
  }
  body {
    overflow: hidden;
  }
  .section {
    display: flex;
    flex-direction: column;
  }
  .blck {
    background-color: #fff;
    position: absolute;
    bottom: 0;
    width: 100%;
    height: 30%;
    z-index: 999;
    display: flex;
    flex-direction: column;
  }
  .map {
    position: relative;
    z-index: 0;
    width: 100%;
    height: 100vw;
  }
  .marker-cluster-small {
    background-color: rgba(181, 226, 140, 0.6);
  }
  .marker-cluster-small div {
    background-color: rgba(110, 204, 57, 0.6);
  }

  .marker-cluster-medium {
    background-color: rgba(241, 211, 87, 0.6);
  }
  .marker-cluster-medium div {
    background-color: rgba(240, 194, 12, 0.6);
  }

  .marker-cluster-large {
    background-color: rgba(253, 156, 115, 0.6);
  }
  .marker-cluster-large div {
    background-color: rgba(241, 128, 23, 0.6);
  }

  /* IE 6-8 fallback colors */
  .leaflet-oldie .marker-cluster-small {
    background-color: rgb(181, 226, 140);
  }
  .leaflet-oldie .marker-cluster-small div {
    background-color: rgb(110, 204, 57);
  }

  .leaflet-oldie .marker-cluster-medium {
    background-color: rgb(241, 211, 87);
  }
  .leaflet-oldie .marker-cluster-medium div {
    background-color: rgb(240, 194, 12);
  }

  .leaflet-oldie .marker-cluster-large {
    background-color: rgb(253, 156, 115);
  }
  .leaflet-oldie .marker-cluster-large div {
    background-color: rgb(241, 128, 23);
  }

  .marker-cluster {
    background-clip: padding-box;
    border-radius: 20px;
  }
  .marker-cluster div {
    width: 30px;
    height: 30px;
    margin-left: 5px;
    margin-top: 5px;

    text-align: center;
    border-radius: 15px;
    font: 12px "Helvetica Neue", Arial, Helvetica, sans-serif;
  }
  .marker-cluster span {
    line-height: 30px;
  }
</style>
