# 🚀 Smart-CI

**Smart-CI** is a tool I built to **optimize CI/CD pipelines** by running only the **tests that matter** based on code changes.  
👉 The goal: **faster feedback for developers** and less time wasted in long pipelines.

---

## 🎯 The Problem

In many teams, pipelines become a **bottleneck**:  
- Unit, functional, and end-to-end tests are all triggered on every commit.  
- Developers wait minutes (sometimes hours) to validate a merge request.  
- Slow feedback cycles block integration and reduce productivity.  

---

## 💡 The Solution

I designed **Smart-CI** to solve this:  
- A **Dockerized CLI tool** that analyzes the **Git diff**.  
- Automatically detects which files are impacted.  
- Runs **only the relevant tests**.  
- Works with **GitLab, GitHub Actions, Azure DevOps, Jenkins, and more**.  

👉 Result: **faster pipelines, happier developers.**

---

## 🧰 Quick Usage

### Build and run locally

```bash
# Build the Docker image
docker build -t choose_test_ci_cd .

# Run with default diff (origin/HEAD~1 vs HEAD)
docker run --rm choose_test_ci_cd

# Compare two specific commits
docker run --rm choose_test_ci_cd --diff <commit1> <commit2>
```

---

## 🔗 CI/CD Integration

### GitLab CI

```yaml
smart-tests:
  stage: test
  image: docker:latest
  services: [docker:dind]
  script:
    - docker run --rm -v "$CI_PROJECT_DIR":/workspace -w /workspace choose_test_ci_cd         --diff "$CI_MERGE_REQUEST_TARGET_BRANCH_SHA" "$CI_COMMIT_SHA"
    - ./run-selected-tests.sh
```

### Azure DevOps

```yaml
- script: |
    echo "Logging into Docker Hub..."
    echo "$(DOCKER_HUB_PASSWORD)" | docker login -u "$(DOCKER_HUB_USERNAME)" --password-stdin
    docker build -t "$(DOCKER_IMAGE_NAME)" .
    docker push "$(DOCKER_IMAGE_NAME)"
  displayName: 'Docker Login, Build and Push'
```

---

## 🔥 Impact

- Reduced pipeline execution time.  
- Increased developer productivity.  
- Fewer merge request bottlenecks.  
- **Future-ready**: Smart-CI can be extended with AI to analyze dependencies even more intelligently.  

---

## 👨‍💻 My Role

- **Designed** the tool’s architecture (static analysis + CLI).  
- **Developed** the core in Python (Git parsing, dependency analysis).  
- **Dockerized** the tool for seamless CI integration.  
- **Integrated** Smart-CI into GitLab CI and Azure DevOps pipelines.  

---

## 📌 Key Takeaway

Smart-CI showcases my ability to:  
- Identify a **real-world productivity problem**.  
- Build an **elegant technical solution**.  
- Think about **integration and developer workflows**.  
- Deliver something **immediately useful for teams**.  
