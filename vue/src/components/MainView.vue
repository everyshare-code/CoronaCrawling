<template>
    <!-- As a link -->
    <nav class="navbar bg-body-tertiary px-3">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">서울시 코로나19 주요뉴스</a>
      </div>
    </nav>
    
    <LoadingView v-if="modal"></LoadingView>
    
      <div class="container" >
          <div class="row mt-3">
            <a v-for="category, idx in categories" :key="category" class="col btn rounded me-2 d-flex align-items-center justify-content-center" :class="[isActive[idx]?'btn-secondary':'btn-outline-secondary']" @click.prevent="fetchNews(idx)" >
              {{ category }}
            </a>
          </div>
          <div class="container mt-3" v-if="complete">
          <ContentView v-for="content in contents" :key="content" :content-data="content"></ContentView>
          </div>
      </div>
  </template>
  <script>
  import { mapActions, mapState } from 'vuex'
  import ContentView from '@/components/ContentView.vue'
  import LoadingView from '@/components/LoadingView.vue'
  
  export default {
    components:{
      ContentView,
      LoadingView
    },
    data() {
      return{
        isActive:[],
        complete:false,
        modal:true,
        categories:['전체','재택치료/외래진료','백신접종','경제지원','코로나19 생활정보','코로나검사치료','온라인문화생활','사회적거리두기'],
        contents:null
      }
    },
    computed: {
      ...mapState({
        contents: state => state.newsData
      })
    },
    methods: {
      ...mapActions(['fetchNewsData']),
      fetchNews(idx) {
        this.isActive.fill(false);
        this.isActive[idx] = true;
        this.modal = true;

        this.fetchNewsData(idx)
          .then(data => {
            this.contents = data;  // 스토어에서 또는 요청 결과에서 데이터 할당
            this.complete = true;
            this.modal = false;
          })
          .catch(error => console.log(error));
    },
    initialize() {
      this.fetchNews(null);
    }
    },
    mounted(){
        this.isActive=new Array(this.categories.length).fill(false);
        this.initialize();
    }
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
    .btn {
        font-size: 0.8em;
    }
  </style>