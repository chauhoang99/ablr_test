const template = `
    <div class="container">
        <tabs>
            <tab name="Contact Info" :selected="true">
                <div class="field">
                    <label class="label">Mobile Number</label>
                    <input class="input" type="text" :value="retrieved_data.mobileno.nbr.value">
                </div>
                <div class="field">
                    <label class="label">Block Number</label>
                    <input
                        class="input"
                        type="text"
                        :value="retrieved_data.regadd.block.value"
                    >
                </div>
                <div class="field">
                    <label class="label">Street Name</label>
                    <input class="input" type="text" :value="retrieved_data.regadd.street.value">
                </div>
                <div class="field">
                    <label class="label">Building Name</label>
                    <input class="input" type="text" :value="retrieved_data.regadd.building.value">
                </div>
                <div class="field">
                    <label class="label">Floor and Unit Number</label>
                    <input class="input" type="text" :value="'#' + retrieved_data.regadd.floor.value + '-' + retrieved_data.regadd.unit.value">
                </div>
                <div class="field">
                    <label class="label">Postal Code</label>
                    <input class="input" type="text" :value="retrieved_data.regadd.postal.value">
                </div>
                <div class="field">
                    <label class="label">Type of Housing</label>
                    <input class="input" type="text" :value="retrieved_data.hdbtype.desc">
                </div>
            </tab>
            <tab name="Personal Info">
                <div class="field">
                    <label class="label">NRIC/FIN</label>
                    <input class="input" type="text" :value="retrieved_data.uinfin.value">
                </div>
                <div class="field">
                    <label class="label">Principal Name</label>
                    <input class="input" type="text" :value="retrieved_data.name.value">
                </div>
                <div class="field">
                    <label class="label">Sex</label>
                    <input class="input" type="text" :value="retrieved_data.sex.desc">
                </div>
                <div class="field">
                    <label class="label">Date of Birth</label>
                    <input class="input" type="text" :value="retrieved_data.dob.value">
                </div>
                <div class="field">
                    <label class="label">Country of Birth</label>
                    <input class="input" type="text" :value="retrieved_data.birthcountry.desc">
                </div>
                <div class="field">
                    <label class="label">Recidential Status</label>
                    <input class="input" type="text" :value="retrieved_data.residentialstatus.desc">
                </div>
                <div class="field">
                    <label class="label">Nationality</label>
                    <input class="input" type="text" :value="retrieved_data.nationality.desc">
                </div>
                <div class="field">
                    <label class="label">Race</label>
                    <input class="input" type="text" :value="retrieved_data.race.desc">
                </div>
            </tab>
            <tab name="Income Info">
                <div class="field">
                    <label class="label">Notice of Assessment History</label>
                    <table class="table">
                        <thead>
                            <tr>
                              <th>Year of Assessment</th>
                              <th>Employment</th>
                              <th>Trade</th>
                              <th>Interest</th>
                              <th>Rent</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="year in retrieved_data.noahistory.noas" v-bind:key="year.yearofassessment.value">
                                <td>{{ year.yearofassessment.value }}</td>
                                <td>{{ year.employment.value }}</td>
                                <td>{{ year.trade.value }}</td>
                                <td>{{ year.interest.value }}</td>
                                <td>{{ year.rent.value }}</td>
                        </tbody>
                    </table>
                </div>
                <div class="field">
                    <label class="label">Other Income Information</label>
                    <input class="input" type="text" :value="retrieved_data.ownerprivate.value">
                </div>
                <div class="field">
                    <label class="label">CPF Account Balance</label>
                    <div v-if="retrieved_data.cpfbalances.unavailable">
                    Unavailable
                    </div>
                    <div v-else>
                        <label class="label">Ordinary Account (OA) (S$)</label>
                        <input class="input" type="text" :value="retrieved_data.cpfbalances.oa.value">
                        <label class="label">Special Account (SA) (S$)</label>
                        <input class="input" type="text" :value="retrieved_data.cpfbalances.sa.value">
                        <label class="label">Medisave Account (MA) (S$)</label>
                        <input class="input" type="text" :value="retrieved_data.cpfbalances.ma.value">
                    </div>
                </div>
                <div class="field">
                    <label class="label">CPF Contribution History</label>
                    <table class="table">
                        <thead>
                            <tr>
                              <th>For Month</th>
                              <th>Paid On</th>
                              <th>Amount</th>
                              <th>Employer</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="month in retrieved_data.cpfcontributions.history" v-bind:key="month.month.value">
                                <td>{{ month.month.value }}</td>
                                <td>{{ month.date.value }}</td>
                                <td>{{ month.amount.value }}</td>
                                <td>{{ month.employer.value }}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </tab>
        </tabs>
    </div>
`

import Tabs from './tabs/tabs.js'
import Tab from './tab/tab.js'

export default {
    template,
    data () {
        return {
          retrieved_data: JSON.parse(document.getElementById('retrieved-data').textContent)
        }
    },
    components: {
        'tabs': Tabs,
        'tab': Tab
    }
}