import uvicorn

import settings

if __name__ == '__main__':
    uvicorn.run(
        'app:api',
        host=settings.API_HOST,
        port=settings.API_PORT,
        log_level=settings.API_LOG_LEVEL,
        reload=settings.API_RELOAD,
        workers=settings.WEB_CONCURRENCY,
    )
