def dockerize_package(ctx, os, host):
    from canari.commands.dockerize_package import dockerize_package
    dockerize_package(ctx.project, os, host)