<script>
import { Line } from 'vue-chartjs'

export default {
  extends: Line,
  props: {

    datacollection: {
      type: Object,
      default: null
    },
    options: {
      type: Object,
      default: null
    }
  },
  data: () => ({
    
  }),
  mounted () {
      console.log(`[LineChartComponent] - ${this.datacollection} - ${this.options}`)
      this.renderChart(this.datacollection, this.options)
    
  },
}
</script>

<style>
</style>