async def verify_docker_worker_task(chain, link):
    if chain != link:
        check_interactive_docker_worker(link)
        verify_docker_image_sha(chain, link)