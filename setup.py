import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='yc_cloud_logging_handler',
    version='0.1.0',
    author='Vitaly Khabarov',
    author_email='vitkhab@gmail.com',
    description='Logging handler for Yandex.Cloud Cloud Logging solution',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/vitkhab/yc_cloud_logging_handler',
    project_urls = {
        "Bug Tracker": "https://github.com/vitkhab/yc_cloud_logging_handler/issues"
    },
    license='MIT',
    packages=['yc_cloud_logging_handler'],
    install_requires=['python-yandex-cloud-logging', 'yandexcloud'],
)