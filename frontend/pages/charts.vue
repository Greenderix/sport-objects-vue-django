<template>
    <section>
        <a href="/">
            <button>На главную</button>
        </a>
        <div class="status-chart">
            <div class="info">
                <h1>График статуса спортивных объектов</h1>
                <p>Всего активных: {{ numActice }}</p>
                <p>Всего неактивных: {{ numPassive }}</p>
            </div>
            <ul class="chart">
                <li>
                    <span :style="styleActive" title="Активные объекты"></span>
                </li>
                <li>
                    <span :style="stylePassive" title="Неактивные объекты"></span>
                </li>
            </ul>
        </div>
        <div class="status-chart">
            <div class="info">
                <h1>График количества объектов в Москве</h1>
                <p>Всего объектов: {{ numMoscow }}</p>
            </div>
            <ul class="chart">
                <li>
                    <span style="height: 100%;" title="Объектов в москве"></span>
                </li>
            </ul>
        </div>
    </section>
</template>

<script>
export default {
    data: () => ({
        numActice: 70,
        numPassive: 30,
        numMoscow: 0,
    }),
    computed: {
        styleActive() {
            return 'height: ' + (this.numActice/(this.numActice+this.numPassive)*100) + '%'; 
        },
        stylePassive() {
            return 'height: ' + (this.numPassive/(this.numActice+this.numPassive)*100) + '%'; 
        }
    },
    methods: {
        async respActive(){
            try{
                await this.$axios.get("/objects?search=Y").then(response => (this.numActice = response.data.length));
            }
            catch (e) {
                console.log(e)
            }
        },
        async respPassive(){
            try{
                await this.$axios.get("/objects?search=N").then(response => (this.numPassive = response.data.length));
            }
            catch (e) {
                console.log(e)
            }
        },
        async respMoscow(){
            try{
                await this.$axios.get("/objects?search=Москва").then(response => (this.numMoscow = response.data.length));
            }
            catch (e) {
                console.log(e)
            }
        },
    },
    mounted() {
        this.respMoscow();
        this.respActive();
        this.respPassive();
    }
}
</script>

<style>
.status-chart {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 20px 40px 40px 40px;
    width: 100%;
    border-bottom: 1px solid #808080;
}
.chart{
  display:table;
  table-layout: fixed;   
  
  width:60%;
  max-width:700px;
  height:200px;
  margin:0 auto;
  
  background-image:linear-gradient(to top, rgba(0, 0, 0, 0.1) 2%, transparent 2%);
  background-size: 100% 50px;
  background-position: left top;
}
  
li{
    position: relative;
    display:table-cell;
    vertical-align:bottom;
    height:200px;
}

span{
    margin:0 1em;
    display: block;
    background-color: rgba(7, 130, 192, 0.4);
    animation: draw 1s ease-in-out;  
}
span:before{
    position:absolute;
    left: 0;
    right: 0;
    top: 100%;
    padding:5px 1em 0;
    display:block;
    text-align:center;
    content:attr(title);
    word-wrap: break-word;
}
  

@keyframes draw{
  0%{height:0;} 
}
</style>