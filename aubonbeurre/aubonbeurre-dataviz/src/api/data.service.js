// Singleton Class
export let APIService = ( function(){
    let instance = null;
    const API_URL = 'http://localhost:3009'

    // constructor
    let constructor = function(){
        // define all methods and attribute which are not static here

        /**
         * GET AUTOMATE RECORDS FROM UNIT
         */
        this.getAutomateRecordsFromUnit = function(unitNumber) {
            return new Promise((resolve, reject) => {
                const url = `${API_URL}/complete-unit-recording/${unitNumber}`;

                console.log('[APIService] - getAutomateRecordsFromUnit - start', unitNumber);
                fetch(url, {
                    method:'get',
                    headers:{
                        'Content-Type':'application/json'
                    },
                }).then(res => {
                    console.log('[APIService] - getAutomateRecordsFromUnit - res', res);
                    return res.json();
                }).then(data => {
                    console.log('[APIService] - getAutomateRecordsFromUnit - data', data);
                    resolve(data);
                }).catch(error => {
                    console.error('[APIService] - ', error);
                    reject(error);
                })
            })
        }
    }

    //Instance accessor
    return new function(){
        this.getInstance = function(){
            if( instance == null ){
                instance = new constructor();
                instance.constructor = null;
            }

            return instance;
        }
    }
})();