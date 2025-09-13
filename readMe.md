User : 










Setup CI Team : 


build : 
docker build -t choose_test_ci_cd .

run : 
docker run --rm choose_test_ci_cd 

full command :
docker run --rm choose_test_ci_cd --diff origin/HEAD~1 HEAD

specify the commit : 
docker run --rm choose_test_ci_cd --diff commit1 commit2 


by default : --diff origin/HEAD~1 HEAD


for gitlab : 


    - script: |
        echo "Logging into Docker Hub..."
        echo "$(DOCKER_HUB_USERNAME)"
        echo "$(DOCKER_HUB_PASSWORD)" | docker login -u "$(DOCKER_HUB_USERNAME)" --password-stdin

        echo "Building Docker image..."
        docker build -t "$(DOCKER_IMAGE_NAME)" .

        echo "Pushing Docker image to Docker Hub..."
        docker push "$(DOCKER_IMAGE_NAME)"
      displayName: 'Docker Login, Build and Push'

