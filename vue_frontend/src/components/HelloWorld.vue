<template>
  <section className="bg-gray-50 dark:bg-gray-900">
    <div className="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
      <button className="flex items-center mb-6 text-2xl font-semibold text-gray-900 dark:text-white">
        <img className="w-8 h-8 mr-2" src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/logo.svg" alt="logo" />
        My Scrabble App
      </button>
      <div
        className="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
        <div className="p-6 space-y-4 md:space-y-6 sm:p-8">
          <form className="space-y-4 md:space-y-6" action="#">
            <div>
              <label htmlFor="sentence" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your
                Sentence</label>
              <input v-model="sentence" placeholder="Enter a sentence" required @keyup.enter="transformSentence" id="sentence"
                className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" />
            </div>
            <button type="button" @click="transformSentence"
              className="w-full text-white bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">Convert</button>
            <p v-if="result.original" className="text-sm font-light text-gray-500 dark:text-gray-400">
              Original: <span className="text-primary-600 font-extrabold">{{ result.original }}</span>
            </p>
            <p v-if="result.converted" className="text-sm font-light text-gray-500 dark:text-gray-400">
              Converted: <span className="text-primary-600 font-extrabold">{{ result.converted }}</span>
            </p>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from 'axios';

export default {
  name: 'App',
  data() {
    return {
      sentence: '',
      result: {
        original: '',
        converted: ''
      }
    };
  },
  methods: {
    transformSentence() {
      // use axios to call endpoint
      axios.post('/convert/', { sentence: this.sentence })
        .then(response => {
          this.result = response.data;
        })
        .catch(error => {
          console.error('There was an error!', error);
        });
    }
  }
}
</script>

<style>
#app {
  text-align: center;
  margin-top: 50px;
}
</style>
