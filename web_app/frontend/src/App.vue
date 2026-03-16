
<template>
  
  <main>

    <div class="container">

      <h1>Loan Prediction</h1>

      <form class="form">

        <div class="form-group">
          <label>Gender</label>
          <select v-model="form.gender">
            <option value="">Not filled</option>
            <option value="male">Male</option>
            <option value="female">Female</option>
          </select>
        </div>

        <div class="form-group">
          <label>Married</label>
          <select v-model="form.married">
            <option value="">Not filled</option>
            <option value="yes">Yes</option>
            <option value="no">No</option>
          </select>
        </div>

        <div class="form-group">
          <label>Dependents</label>
          <select v-model="form.dependents">
            <option value="">Not filled</option>
            <option value="0">0</option>
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3+">3+</option>
          </select>
        </div>

        <div class="form-group">
          <label>Education</label>
          <select v-model="form.education">
            <option value="">Not filled</option>
            <option value="graduate">Graduate</option>
            <option value="not graduate">Not Graduate</option>
          </select>
        </div>

        <div class="form-group">
          <label>Self Employed</label>
          <select v-model="form.self_employed">
            <option value="">Not filled</option>
            <option value="yes">Yes</option>
            <option value="no">No</option>
          </select>
        </div>

        <div class="form-group">
          <label>Applicant Income</label>
          <input type="number" v-model.number="form.applicantincome" placeholder="Not filled">
        </div>

        <div class="form-group">
          <label>Co Applicant Income</label>
          <input type="number" v-model.number="form.coapplicantincome" placeholder="Not filled">
        </div>

        <div class="form-group">
          <label>Loan Amount</label>
          <input type="number" v-model.number="form.loanamount" placeholder="Not filled">
        </div>

        <div class="form-group">
          <label>Loan Term</label>
          <input type="number" v-model.number="form.loan_amount_term" placeholder="Not filled">
        </div>

        <div class="form-group">
          <label>Credit History</label>
          <select v-model="form.credit_history">
            <option value="">Not filled</option>
            <option value="yes">Yes</option>
            <option value="no">No</option>
          </select>
        </div>

        <div class="form-group">
          <label>Property Area</label>
          <select v-model="form.property_area">
            <option value="">Not filled</option>
            <option value="urban">Urban</option>
            <option value="semiurban">Semiurban</option>
            <option value="rural">Rural</option>
          </select>
        </div>

        <button class="predict-btn" v-on:click="predictLoan" type="button">
          Predict
        </button>

      </form>

      <div v-if="prediction !== ''" class="result">
        Prediction: <strong>{{ prediction }}</strong>
      </div>

    </div>

  </main>

</template>




<script>

import axios from "axios"

export default {


  data() {
    return {

      form: {
        gender: "",
        married: "",
        dependents: "",
        education: "",
        self_employed: "",
        applicantincome: null,
        coapplicantincome: null,
        loanamount: null,
        loan_amount_term: null,
        credit_history: "",
        property_area: ""
      },

      prediction: "",

      API: import.meta.env.VITE_API_URL

    }
  },


  methods: {

    async predictLoan(){

      try{

        this.prediction = ""

        const cleanedData = {}

        for(const key in this.form){

          const value = this.form[key]

          if(value !== "" && value !== null){
            cleanedData[key] = value
          }

        }

        const result = await axios.post("api/get-loan-prediction", cleanedData)

        this.prediction = result.data.predition

      }catch(err){

        const error = err.response?.data?.detail

        if (Array.isArray(error)) {
          alert(error.map(e => e.msg).join("\n"))
        } else {
          alert(error || "Server error")
        }

      }

    }

  }

}

</script>




<style>

*{
  margin: 0;
  padding: 0;
  box-sizing:border-box;
}

main{
  width:100%;
  min-height:100vh;
  background:linear-gradient(135deg,#dfe9f3,#ffffff);
  display:flex;
  justify-content:center;
}

.container{
  width:100%;
  max-width:700px;
  background:white;
  padding:45px;
  margin:70px 20px 100px 20px;
  border-radius:16px;
  box-shadow:0 25px 50px rgba(0,0,0,0.12);
}

h1{
  text-align:center;
  margin-bottom:40px;
  font-size:30px;
  font-weight:600;
  color:#2c3e50;
}

.form{
  display:grid;
  grid-template-columns:1fr 1fr;
  gap:22px;
}

.form-group{
  display:flex;
  flex-direction:column;
}

.form-group label{
  font-size:14px;
  font-weight:500;
  margin-bottom:6px;
  color:#555;
}

input, select{
  padding:12px 14px;
  border-radius:10px;
  border:1px solid #d0d7de;
  font-size:14px;
  background:#f8fafc;
  transition:all 0.2s ease;
}

input:focus, select:focus{
  outline:none;
  border-color:#3b82f6;
  background:white;
  box-shadow:0 0 0 3px rgba(59,130,246,0.15);
}

input::placeholder{
  color:#9aa3af;
}

.predict-btn{
  grid-column:span 2;
  margin-top:10px;
  padding:14px;
  border:none;
  border-radius:12px;
  font-size:16px;
  font-weight:600;
  color:white;
  background:linear-gradient(135deg,#3b82f6,#2563eb);
  cursor:pointer;
  transition:all 0.25s ease;
}

.predict-btn:hover{
  transform:translateY(-2px);
  box-shadow:0 10px 20px rgba(37,99,235,0.35);
}

.result{
  margin-top:35px;
  padding:20px;
  border-radius:12px;
  text-align:center;
  font-size:20px;
  font-weight:600;
  background:#f1f5ff;
  border:1px solid #dbe4ff;
  color:#1e3a8a;
}

@media (max-width: 768px){

  .form{
    grid-template-columns:1fr;
  }

  .predict-btn{
    grid-column:span 1;
  }

}

@media (max-width: 500px){

  h1{
    font-size:24px;
  }

  .container{
    padding:25px;
    margin:20px 10px;
  }

  input, select{
    padding:10px;
  }

  .predict-btn{
    padding:12px;
    font-size:15px;
  }

}

</style>