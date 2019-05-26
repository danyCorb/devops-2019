<script>
  let { APIService } = require('../../api/data.service.js')
  let LineChart = require('../../components/LineChart.vue').default

  module.exports = {
    name: 'data-visualizer-page',
    components: {LineChart},
    props: [],
    data () {
      return {
        selectedUnitNumber: 1,
        selectedAutomateNumber: 1,
        unitNumbers: [1],
        automateNumbers: [1,2,3,4,5],
        refresher: false,
        // Charts options
        options: {
          responsive: true,
          maintainAspectRatio: false,
          animation: false,
        },
        // Charts style
        myStyles: {
          height: '150px',
          width: '45%',
          position: 'relative'
        }
      }
     
      
    },
    computed: {
      // Mock the data of one unit
      completeUnitRecording: {
        get: function () {
          return this.getMockedCompleteUnitRecording();
        }
      }
    },
    asyncComputed: {

      // Contain all data from one unit. This value is refreshed every minutes in mounted method thanks to the refresher boolean
      datacollections: {
        
        get () {
          return new Promise((resolve, reject) => {
            const fakeRefresher = !this.refresher
            APIService.getInstance().getAutomateRecordsFromUnit(this.selectedUnitNumber).then( data => {
              resolve(this.getAllDataCollections(data, this.selectedAutomateNumber))
            })
          })
        },
        default: []
        
      }
    },
    mounted () {
      console.log('[DataVisualizerVue] - mounted')

      // Modify a value that used to calculate data in graphs every minutes. 
      this.$nextTick(function () {
          window.setInterval(() => {
            console.log("Bonsoir")
            this.refreshAPIData()
          },60000);
      })
    
    },
    methods: {
      // reload data when user change unit with select element
      onUnitChange(event) {
        console.log(`[DataVisualizerVue] - unit changed ${JSON.stringify(event.target.value)}`)

        this.selectedUnitNumber = Number(event.target.value)
        this.refreshAPIData()
        
      },
      // change chart data to correspond to the selected automate
      onAutomateChange(event) {
        console.log(`[DataVisualizerVue] - automate changed`)
        
        this.selectedAutomateNumber = Number(event.target.value)
        this.refreshAPIData()
      },


      refreshAPIData(){
        this.refresher = !this.refresher;
      },

      // get mocked data
      getMockedCompleteUnitRecording() {
        return [
          {
            number: 1,
            type: 1,
            records: [
              {
                tankTemperature: 1.5,
                externalTemperature: 10.4,
                milkTankWeight: 1.5,
                finalProductWeight: 1.4,
                phMeasurement: 2.3,
                kPosMeasurement: 4,
                naClConcentration: 4.5,
                salmonellaLevel: 1,
                eColiLevel: 1,
                listeriaLevel: 2,
              },
              {
                tankTemperature: 1.6,
                externalTemperature: 8.4,
                milkTankWeight: 1.6,
                finalProductWeight: 1.0,
                phMeasurement: 2.7,
                kPosMeasurement: 3,
                naClConcentration: 4.2,
                salmonellaLevel: 2,
                eColiLevel: 2,
                listeriaLevel: 1,
              }
            ]
          },
          {
            number: 2,
            type: 3,
            records: [
              {
                tankTemperature: 16,
                externalTemperature: 10.4,
                milkTankWeight: 1.5,
                finalProductWeight: 1.4,
                phMeasurement: 2.3,
                kPosMeasurement: 4,
                naClConcentration: 4.5,
                salmonellaLevel: 1,
                eColiLevel: 1,
                listeriaLevel: 2,
              },
              {
                tankTemperature: 1.6,
                externalTemperature: 8.4,
                milkTankWeight: 1.6,
                finalProductWeight: 1.0,
                phMeasurement: 2.7,
                kPosMeasurement: 3,
                naClConcentration: 4.2,
                salmonellaLevel: 2,
                eColiLevel: 2,
                listeriaLevel: 1,
              }
            ]
          }
        ]
      },

      // format data for the charts, for one automate
      getAllDataCollections(completeUnitRecording, automateNumber) {
        console.log(`[DataVisualizer] - complete unit recording`, automateNumber)
        console.log(completeUnitRecording)

        // Get only data collections for one automate
        const completeAutomateRecord = completeUnitRecording.find( el => el.number === automateNumber)

        console.log(`[DataVisualizer] - complete automate record`)
        console.log(completeAutomateRecord)

        console.log(`Object keys - ${ Object.keys(completeAutomateRecord.records[0])}`)

        const keys = Object.keys(completeAutomateRecord.records[0]).filter(key => !key.includes('id'))

        // generate the data set for each attribute
        const attributeDataSets = keys.map(key => {
          const data = completeAutomateRecord.records.map(record => record[key])
          const label = key
          const backgroundColor = '#f87979'

          return {label, backgroundColor, data}
        })

        // TO DO : CHANGE WITH RECORD DATE
        const labels = []

        for (let i=1; i <= completeAutomateRecord; i++) {
          labels.push(i.toString())
        }

        const datacollections = attributeDataSets.map(dataset => {
          const datasets = [dataset]
          return {labels, datasets}
        })

        console.log(`[DataVisualizer] - datacollections`)
        console.log(datacollections)

        // this.datacollections = datacollections
        return datacollections
      },
    }
  }
    
</script>

<template>
  <section class="data-visualizer-page">

    <form id="form">
      <!-- Unit select -->
      <label>Unit number</label>
      <select v-model="selectedUnitNumber" @change="onUnitChange($event)">
        <option v-for="unitNumber in unitNumbers" :key="unitNumber">{{unitNumber}}</option>
      </select>

      <!-- Automate select -->
      <label>Automate number</label>
      <select v-model="selectedAutomateNumber" @change="onAutomateChange($event)">
        <option v-for="automateNumber in automateNumbers" :key="automateNumber">{{automateNumber}}</option>
      </select>
    </form>

    <div id="line-charts-container">
      <LineChart 
        :styles="myStyles"
        v-for="(datacollection, i) in this.datacollections"
        class="small"
        :datacollection=datacollection
        :options=options
        v-bind:key="i"
      >
      </LineChart>
    </div>    
    

  </section>
</template>

<style>
  .data-visualizer-page {

  }

  #form {
    display: flex;
    background-color:mediumseagreen;
    color: white;
    padding: 20px;
    justify-content: center;
    align-items: center;

  }

  #form select {
    margin: 0 20px;
  }

  .small {
    position:relative
  }

  .chartjs-render-monitor {
    
  }

  #line-charts-container {
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    flex-direction: row;
    justify-content: space-around;
    color: white;
  }
</style>