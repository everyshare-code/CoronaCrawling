<template>
      <div v-if="contentData && contentData.title && contentData.img" class="card mb-3 mt-3" @click.prevent="detailView(contentData.link)">
    <div class="row g-0">
      <div class="col-md-4">
        <img :src="contentData.img" class="w-100 h-100 object-fit-cover" alt="">
      </div>
      <div class="col-md-8">
        <div class="card-body">
          <h5 class="card-title"><b>{{ contentData.title }}</b></h5>
          <p class="card-text">{{ contentData.summary }}</p>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  props: {
    contentData: {
      type: Object,
      required: false
    }
  },
  methods:{
    detailView(link){
      window.location.href = link;
    }
  }
}
</script>

<style scoped>
  .card-text {
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;  
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .card:hover {
    cursor: pointer;
  }

</style>