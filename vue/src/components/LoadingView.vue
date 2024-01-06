User
<template>
    <div class="modal-backdrop justify-content-center align-items-center d-flex">
        <div class="progress w-50" role="progressbar" aria-label="Animated striped example" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100">
        <div class="progress-bar progress-bar-striped progress-bar-animated" :style="{ width: progress + '%' }">
            Crawling...
        </div>
        </div>
    </div>
  
</template>
<script>
export default {
  data() {
    return {
      progress: 0,
      interval: null // 인터벌을 저장할 변수
    };
  },
  mounted() {
    this.startProgress();
  },
  methods: {
    startProgress() {
      this.interval = setInterval(() => {
        if (this.progress < 100) {
          this.progress += 6;
        } else {
          clearInterval(this.interval); // progress가 100에 도달하면 인터벌을 멈춤
        }
      }, 500);
    }
  },
};
</script>
<style scoped>
    .modal-backdrop {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.5); /* 반투명 배경 */
        z-index: 1050; /* 필요에 따라 조절 */
    }
</style>