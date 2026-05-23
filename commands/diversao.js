async function modalSubmit(interaction) {

    if (interaction.customId !== "confissao_modal") return;

    const confession =
        interaction.fields.getTextInputValue("confissao");

    const logs =
        interaction.client.channels.cache.get(LOGS_CHANNEL_ID);

    const channel =
        interaction.client.channels.cache.get(CONFISSOES_CHANNEL_ID);

    // pega mensagens do canal
    const fetchedMessages = await channel.messages.fetch({
        limit: 100
    });

    // transforma em array
    const messages = Array.from(fetchedMessages.values());

    // escolhe uma mensagem aleatória
    const selected =
        messages[
            Math.floor(Math.random() * messages.length)
        ];

    // reage com tomate
    try {
        await selected.react("🍅");
    } catch {}

    // envia confissão
    await channel.send(
        createMessage({
            title: "📜 Confissão Anônima",
            description: confession,
            footer: "Confissão enviada anonimamente"
        })
    );

    // envia logs
    await logs.send(
        createMessage({
            title: "📜 Nova Confissão",
            fields: [
                {
                    name: "Usuário",
                    value:
                        `${interaction.user.tag} (${interaction.user.id})`
                },
                {
                    name: "Servidor",
                    value: interaction.guild.name
                },
                {
                    name: "Texto",
                    value: confession
                }
            ]
        })
    );

    // responde ao usuário
    await interaction.reply(
        createMessage({
            title: "✅ Confissão enviada",
            description:
                "Sua confissão foi enviada anonimamente."
        })
    );
}