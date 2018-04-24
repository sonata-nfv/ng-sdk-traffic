pipeline {
  agent any
  stages {
    stage('Container Build') {
      steps {
        echo 'Building..'
        sh 'docker build -f ./Dockerfile -t registry.sonata-nfv.eu:5000/tng-sdk-traffic .'
      }
    }
    stage('Unit Tests') {
      steps {
        echo 'Unit Testing..'
        sh 'docker run -i --rm registry.sonata-nfv.eu:5000/tng-sdk-traffic pytest -v'
      }
    }
    stage('Code Style check') {
      steps {
        echo 'Checking code style....'
      }
    }
    stage('Container publishing') {
        steps {
            echo 'Publishing docker image....'
            sh 'docker push registry.sonata-nfv.eu:5000/tng-sdk-traffic'
        }
    }
    stage('Deployment in Integration') {
      steps {
        echo 'Deploying in integration...'
      }
    }
    stage('Smoke Tests') {
      steps {
        echo 'Performing Smoke Tests....'
      }
    }
    stage('Publish Results') {
      steps {
        echo 'Publish Results...'
      }
    }
  }
}
