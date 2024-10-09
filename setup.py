from setuptools import setup, find_packages


def get_packages():
    # packages = ['examples', 'uploader', 'utils', 'uploader.bilibili_uploader', 'uploader.douyin_uploader',
    #             'uploader.ks_uploader', 'uploader.tencent_uploader', 'uploader.tk_uploader', 'uploader.xhs_uploader']
    # new_packages = ["social_auto_upload." + item for item in packages]
    # new_packages.append("social_auto_upload")
    # return new_packages
    packages = find_packages()
    print(packages)
    return packages


setup(
    name='social_auto_upload',
    version='1.0.0',
    packages=get_packages(),
    install_requires=[
    ],
    include_package_data=True,
    package_data={
        'social_auto_upload.utils': ['*.js']
    }
)
